

import json


with open("base1output.json", "r+") as jsonFile:
    data = json.load(jsonFile)
    jsonFile.close()



    for key1, key2 in data.items():
        variable = "mobile"
        if key1 == 'children':
            for key3 in key2:
                for key4,key5 in key3.items():
                    if key4 == 'children':
                        for key6 in key5:
                            for key7,key8 in key6.items():
                                if key7 == 'children':
                                    for key9 in key8:
                                        for key10,key11 in key9.items():
                                            if key10 == 'children':
                                                for key12 in key11:
                                                    for key13,key14 in key12.items():
                                                        if key13 == 'children':
                                                            for key15 in key14:
                                                                for key16,key17 in key15.items():
                                                                    if key16 == 'content':
                                                                        key15[key16] = variable
                                                                        # print(key15[key16])
                                                                        

                                                                        
                                                                        
                                                                        
                                                                        

                # for b,c in a.items():
                    # print(b)
            #     if a == 'children':
            #         for c in b:
            #             for d,e in c.items():
            #                 if d == 'children':
            #                     for f in e:
            #                         for g,h in f.items():
            #                             if g == 'name':
            #                                 print(h)

    # tmp = data["location"]
    # data["location"] = "NewPath"

# jsonFile.seek(0)  # rewind
# json.dump(data, jsonFile)
# jsonFile.truncate()


# with open("final1output.json", "w") as jsonFile:
#     json.dump(data, jsonFile)


# jsonFile = open("base1output.json", "w+")
# jsonFile.write(json.dumps(data))
# jsonFile.close()