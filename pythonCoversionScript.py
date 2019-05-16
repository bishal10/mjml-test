import json
import requests
# import sys
import os

headers = {
    'X-FIGMA-TOKEN': '13179-4a5fb572-ce12-4229-a32e-7f73e629798f',
}

response = requests.get('https://api.figma.com/v1/files/cPNiRry51GKqelElGqLt6MLj', headers=headers).json()
y = json.dumps(response, indent=4)

# looping through the json data to get section data
data1 = response['document']['children'][0]['children'][0]['children']

# base variables contains the minimal base code of the mjml
# base = {u'attributes': {}, u'children': [{u'attributes': {}, u'children': [{u'attributes': {u'font-size': u'13px', u'background-color': u'#fce7b4'}, u'children': [], u'tagName': u'mj-container'}], u'tagName': u'mj-body'}], u'tagName': u'mjml'}
base = {u'attributes': {}, u'children': [{u'attributes': {}, u'children': [{u'attributes': {u'background-color': u''}, u'children': [], u'tagName': u'mj-container'}], u'tagName': u'mj-body'}], u'tagName': u'mjml'}


# looping through the base dictionary to add section as a children components
output_data = base['children'][0]['children'][0]['children']



# function to triger the text section in the base file
def textSection(text_pass,text_pass2,text_pass3,text_pass4,text_pass5):
    # section variable contains the base code of section
    section = {u'attributes': {u'padding-top': u'', u'background-color': u'#2D3445', u'padding-bottom': u''}, u'children': [{u'attributes': {u'width': u'', u'vertical-align': u'top'}, u'tagName': u'mj-column'}], u'tagName': u'mj-section'}
    finalSection = section['children'][0]

    # text variable contains the text block to be added on base code of section
    text = [{u'content': u'HELLO World', u'attributes': {u'font-size': u'', u'width': u'', u'color': u'#ABCDEA', u'align': u'', u'padding-right': u'', u'padding-bottom': u'', u'padding-top': u'', u'font-family': u'', u'padding-left': u''}, u'tagName': u'mj-text'}]

    for key,value in text[0].items():
        if key == "content":
            text[0][key] = text_pass
        # print(key, value )
        if key == "attributes":
            for key1,value1 in text[0]['attributes'].items():
                if key1 == "font-size":
                    text[0]['attributes'][key1] = str(text_pass2) + "px"

            for key2,value2 in text[0]['attributes'].items():
                if key2 == "font-family":
                    text[0]['attributes'][key2] = text_pass3

            for key3,value3 in text[0]['attributes'].items():
                if key3 == "align":
                    text[0]['attributes'][key3] = text_pass4

            for key4,value4 in text[0]['attributes'].items():
                if key4 == "width":
                    text[0]['attributes'][key4] = str(text_pass5) + "px"

    finalSection['children'] = text
    output_data.append(dict(section))

    # throwing output to final.json file
    jsonFile = open("final.json", "w+")
    jsonFile.write(json.dumps(base))
    jsonFile.close()

# function to add button section
def buttonSection(button_text,text_pass5,text_pass8,text_pass9):
    section = {u'attributes': {u'padding-top': u'', u'background-color': u'#2D3445', u'padding-bottom': u''}, u'children': [{u'attributes': {u'width': u'', u'vertical-align': u'top'}, u'tagName': u'mj-column'}], u'tagName': u'mj-section'}
    finalSection = section['children'][0]

    # block containing button base structure
    button_section = [{u'content': u'', u'height':u'', u'attributes': {u'border-radius': u'', u'width':u'', u'height':u'', u'font-size': u'', u'font-family': u'', u'color': u'#FFFFFF', u'align': u'', u'padding': u'', u'padding-right': u'', u'padding-bottom': u'', u'padding-top': u'', u'background-color': u'#E9703E', u'padding-left': u''}, u'tagName': u'mj-button'}]

    for key,value in button_section[0].items():
        if key == "content":
            button_section[0][key] = button_text

    for key3,value3 in button_section[0]['attributes'].items():
        if key3 == "align":
            button_section[0]['attributes'][key3] = text_pass9

    for key4,value4 in button_section[0]['attributes'].items():
        if key4 == "width":
            button_section[0]['attributes'][key4] = str(text_pass5) + "px"

    for key5,value5 in button_section[0]['attributes'].items():
        if key5 == "height":
            button_section[0]['attributes'][key5] = str(text_pass8) + "px"

    # for key2,value2 in text[0]['attributes'].items():
    #     if key2 == "padding-top":
    #         button_section[0]['attributes'][key2] = str(text_pass6) + "px"
    #
    # for key6,value6 in text[0]['attributes'].items():
    #     if key6 == "padding-left":
    #         button_section[0]['attributes'][key6] = str(text_pass7) + "px"

    finalSection['children'] = button_section

    output_data.append(dict(section))

    # throwing output to final.json file
    jsonFile = open("final.json", "w+")
    jsonFile.write(json.dumps(base))
    jsonFile.close()

# function to add line segment
def lineElement(text_pass5,text_pass8,text_pass9):

    section = {u'attributes': {u'padding-top': u'', u'background-color': u'#2D3445', u'padding-bottom': u''}, u'children': [{u'attributes': {u'width': u''}, u'tagName': u'mj-column'}], u'tagName': u'mj-section'}
    finalSection = section['children'][0]

    # code block of line structure
    line = [{u'attributes': {u'border-width': u'', u'border-style': u'solid', u'border-color': u'#565F73', u'width': u''}, u'tagName': u'mj-divider'}]

    for key,value in line[0]['attributes'].items():
        if key == "width":
            line[0]['attributes'][key] = str(text_pass5) + "px"

    for key5,value5 in line[0]['attributes'].items():
        if key5 == "border-width":
            line[0]['attributes'][key5] = str(text_pass8) + "px"


    # for key5,value5 in line[0]['attributes'].items():
    #     if key5 == "padding-top":
    #         line[0]['attributes'][key5] = str(text_pass6) + "px"
    #
    # for key6,value6 in line[0]['attributes'].items():
    #     if key6 == "padding-left":
    #         line[0]['attributes'][key6] = str(text_pass7) + "px"

    finalSection['children'] = line
    output_data.append(dict(section))

    # json output file
    jsonFile = open("final.json", "w+")
    jsonFile.write(json.dumps(base))
    jsonFile.close()

# function to triger the element in the base file
def imageElement(image_pass,text_pass4,text_pass5,text_pass8,text_pass9):
    section = {u'attributes': {u'padding-top': u'', u'background-color': u'#2D3445', u'padding-bottom': u''}, u'children': [{u'attributes': {u'width': u'', u'vertical-align': u'top'}, u'tagName': u'mj-column'}], u'tagName': u'mj-section'}
    finalSection = section['children'][0]

    image = [{u'attributes': {u'src': u'', u'align':u'', u'width':u'', u'height':u'', u'padding-left': u'', u'padding-right': u'',u'padding-top': u'', u'padding-bottom': u''}, u'tagName': u'mj-image'}]

    for key,value in image[0]['attributes'].items():
        if key == "src":
            image[0]['attributes'][key] = image_pass

    for key2,value2 in image[0]['attributes'].items():
        if key2 == "width":
            image[0]['attributes'][key2] = str(text_pass5) + "px"

    for key3,value3 in image[0]['attributes'].items():
        if key3 == "align":
            image[0]['attributes'][key3] = text_pass9

    for key5,value5 in image[0]['attributes'].items():
        if key5 == "height":
            image[0]['attributes'][key5] = str(text_pass8) + "px"

    finalSection['children'] = image
    output_data.append(dict(section))

    # json output file
    jsonFile = open("final.json", "w+")
    jsonFile.write(json.dumps(base))
    jsonFile.close()

# loop for text section
image_pass = text_pass = text_pass2 = text_pass3 = text_pass4 = text_pass5 = text_pass8 = button_text = ''
for list1 in data1:
        for key1,value1 in list1.items():
                if key1 == 'children':
                        for key2,value2 in value1[1].items():
                                if key2 == 'characters':
                                    text_pass = value2
                                    # print(key2,value2)

                                if key2 == 'style':
                                    for key3,value3 in value1[1]['style'].items():
                                        if key3 == 'fontSize':
                                            text_pass2 = value3
                                            # print(key3,value3)

                                    for key4,value4 in value1[1]['style'].items():
                                        if key4 == 'fontFamily':
                                            text_pass3 = value4
                                            # print(key4,value4)
                                            # textSection(text_pass,text_pass2,text_pass3)

                                    for key5,value5 in value1[1]['style'].items():
                                        if key5 == 'textAlignHorizontal':
                                            text_pass4 = value5
                                            # print(key5,value5)
                                            textSection(text_pass,text_pass2,text_pass3,text_pass4,text_pass5)

                                if key2 == "absoluteBoundingBox":
                                    for key6,value6 in value1[1]['absoluteBoundingBox'].items():
                                        if key6 == "width":
                                            text_pass5 = value6

                                # if key2 == "absoluteBoundingBox":
                                #     for key7,value7 in value1[1]['absoluteBoundingBox'].items():
                                #         if key7 == "y":
                                #             text_pass6 = value7
                                #             # print(key7,value7)
                                #
                                # if key2 == "absoluteBoundingBox":
                                #     for key8,value8 in value1[1]['absoluteBoundingBox'].items():
                                #         if key8 == "x":
                                #             text_pass7 = value8
                                #             # print(key8,value8)
                                if key2 == "strokeAlign":
                                        text_pass9 = value2

                                if key2 == "absoluteBoundingBox" :
                                    for key9,value9 in value1[1]['absoluteBoundingBox'].items():
                                        if key9 == "height":
                                            text_pass8 = value9
                                            # print (key9,value9)


                                if key2 == "name" and value2 == "section-hrline":
                                    lineElement(text_pass5,text_pass8,text_pass9)

                                if key2 == "name" and value2 == "section-image":
                                    link = 'https://helpx.adobe.com/in/stock/how-to/visual-reverse-image-search/_jcr_content/main-pars/image.img.jpg/visual-reverse-image-search-v2_1000x560.jpg'
                                    imageElement(link,text_pass4,text_pass5,text_pass8,text_pass9)

                                if key2 == "name" and value2 == "section-button-1":
                                    buttonSection(button_text,text_pass5,text_pass8,text_pass9)


os.system("node ./node_modules/.bin/json2mjml final.json outputmjml.mjml")
final_html = os.popen("mjml outputmjml.mjml -o finalhtml.html").read()
