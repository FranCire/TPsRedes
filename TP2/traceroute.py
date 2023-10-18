import sys
from scapy.all import *
from time import *

def write_object_to_file(d,filename):
    with open(filename,"w") as file:
        file.write(str(d))

def read_object_from_file(filename):
    with open(filename,"r") as file:
        lines = file.readlines()
    return eval(lines[0])

def get_bare_traceroute(url,max_ttl,times_per_ttl):
    responses = {}
        
    for ttl in range(1,max_ttl):
        print("TTL",ttl)
        for _ in range(times_per_ttl):
            probe = IP(dst=url, ttl=ttl) / ICMP()
            t_i = time()
            ans = sr1(probe, verbose=False, timeout=0.8)
            t_f = time()
            rtt = (t_f - t_i)*1000
            if ans is not None:

                if ttl not in responses:
                    responses[ttl] = []
                responses[ttl].append((ans.src, rtt))
    

    return responses

def traceroute(url):
    MAX_TTL = 25
    TIMES_PER_TTL = 100
    responses = get_bare_traceroute(url,MAX_TTL,TIMES_PER_TTL)
    write_object_to_file(responses,f"bare_traceroute_{url}.txt")


    processed_responses = {}
    for ttl in responses.keys():
        print("TTL",ttl)
        responders = [response[0] for response in responses[ttl]]
        responder_appearance_count = {responder:responders.count(responder) for responder in responders}
        max_responder = max(responder_appearance_count,key=responder_appearance_count.get)
        all_responder_responses = [response[1] for response in responses[ttl] if response[0] == max_responder]
        average_response_time = sum(all_responder_responses)/len(all_responder_responses)
        processed_responses[ttl] = (max_responder,average_response_time,responder_appearance_count[max_responder])

    write_object_to_file(processed_responses,f"processed_traceroute_{url}.txt")

    rtt_between_jumps = []
    processed_responses[0] = ('0.0.0.0',0)
    cur_ttl = 0

    for ttl in sorted(processed_responses.keys())[1:]:
        if processed_responses[ttl][1] > processed_responses[cur_ttl][1]:
            rtt_between_jumps.append((cur_ttl,ttl,processed_responses[cur_ttl][0],processed_responses[ttl][0],processed_responses[ttl][1] - processed_responses[cur_ttl][1]))
            cur_ttl = ttl
    
    



    
    write_object_to_file(rtt_between_jumps,f"rtt_between_jumps_{url}.txt")





if __name__ == "__main__":
    traceroute("jhu.edu")
    traceroute("cam.ac.uk")
    traceroute("uj.ac.za")
    traceroute("u-tokyo.ac.jp")
