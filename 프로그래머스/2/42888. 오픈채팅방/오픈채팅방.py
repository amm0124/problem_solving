def solution(record):
    answer = []
    record=[list(rec.split()) for rec in record]
    id_dict=dict()
    
    for rec in record :
        if rec[0]=='Enter' or rec[0]=='Change':
            id_dict[rec[1]]=rec[2]

    for rec in record :
        if rec[0]=='Enter' :
            answer.append(f"{id_dict[rec[1]]}님이 들어왔습니다.")
        elif rec[0]=='Leave' :
            answer.append(f"{id_dict[rec[1]]}님이 나갔습니다.")
            
    return answer