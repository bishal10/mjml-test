import json
import requests
# import sys
headers = {
    'X-FIGMA-TOKEN': '11964-dd038e0d-8ac8-4013-a694-e7db037640c4',
}

response = requests.get('https://api.figma.com/v1/files/cPNiRry51GKqelElGqLt6MLj', headers=headers).json()
y = json.dumps(response, indent=4)

# looping through the json data to get section data
data1 = response['document']['children'][0]['children'][0]['children']

# base variables contains the minimal base code of the mjml
base = {u'attributes': {}, u'children': [{u'attributes': {}, u'children': [{u'attributes': {u'font-size': u'13px', u'background-color': u'#fce7b4'}, u'children': [], u'tagName': u'mj-container'}], u'tagName': u'mj-body'}], u'tagName': u'mjml'}

# looping through the base dictionary to add section as a children components
output_data = base['children'][0]['children'][0]['children']



# function to triger the text section in the base file
def textSection(text_pass):

    # section variable contains the base code of section
    section = {u'attributes': {u'padding-top': u'20px', u'background-color': u'#2D3445', u'padding-bottom': u'20px'}, u'children': [{u'attributes': {u'width': u'90%', u'vertical-align': u'top'}, u'tagName': u'mj-column'}], u'tagName': u'mj-section'}
    finalSection = section['children'][0]

    # text variable contains the text block to be added on base code of section
    text = [{u'content': u'HELLO World', u'attributes': {u'font-size': u'13', u'color': u'#ABCDEA', u'align': u'center', u'padding-right': u'25', u'padding-bottom': u'10', u'padding-top': u'10', u'font-family': u'Ubuntu, Helvetica, Arial, sans-serif', u'padding-left': u'25'}, u'tagName': u'mj-text'}]

    for key,value in text[0].items():
        if key == "content":
            text[0][key] = text_pass

    finalSection['children'] = text
    output_data.append(dict(section))

    # throwing output to final.json file
    jsonFile = open("final.json", "w+")
    jsonFile.write(json.dumps(base))
    jsonFile.close()

# function to add button section
def buttonSection(button_text):


    section = {u'attributes': {u'padding-top': u'20px', u'background-color': u'#2D3445', u'padding-bottom': u'20px'}, u'children': [{u'attributes': {u'width': u'90%', u'vertical-align': u'top'}, u'tagName': u'mj-column'}], u'tagName': u'mj-section'}
    finalSection = section['children'][0]

    # block containing button base structure
    button_section = [{u'content': u'Download Receipt', u'attributes': {u'border-radius': u'none', u'font-size': u'14px', u'font-family': u'Helvetica', u'color': u'#FFFFFF', u'align': u'center', u'padding': u'15px 30px', u'padding-right': u'25', u'padding-bottom': u'10', u'padding-top': u'10', u'font-weight': u'bold', u'border': u'none', u'background-color': u'#E9703E', u'padding-left': u'25'}, u'tagName': u'mj-button'}]

    for key,value in button_section[0].items():
        if key == "content":
            button_section[0][key] = button_text


    finalSection['children'] = button_section

    output_data.append(dict(section))

    # throwing output to final.json file
    jsonFile = open("final.json", "w+")
    jsonFile.write(json.dumps(base))
    jsonFile.close()

# function to add line segment
def lineElement():

    section = {u'attributes': {u'padding-top': u'20px', u'background-color': u'#2D3445', u'padding-bottom': u'20px'}, u'children': [{u'attributes': {u'width': u'90%', u'vertical-align': u'top'}, u'tagName': u'mj-column'}], u'tagName': u'mj-section'}
    finalSection = section['children'][0]

    # code block of line structure
    line = [{u'attributes': {u'border-width': u'1px', u'border-style': u'solid', u'border-color': u'#565F73', u'width': u'75%'}, u'tagName': u'mj-divider'}]

    finalSection['children'] = line
    output_data.append(dict(section))

    # json output file
    jsonFile = open("final.json", "w+")
    jsonFile.write(json.dumps(base))
    jsonFile.close()

# function to triger the element in the base file
def imageElement(image_pass):
    section = {u'attributes': {u'padding-top': u'20px', u'background-color': u'#2D3445', u'padding-bottom': u'20px'}, u'children': [{u'attributes': {u'width': u'90%', u'vertical-align': u'top'}, u'tagName': u'mj-column'}], u'tagName': u'mj-section'}
    finalSection = section['children'][0]

    image = [{u'attributes': {u'src': u'http://z2mx.mjt.lu/img/z2mx/b/lhu/rwt.png', u'align':u'center', u'border':u'none', u'width':u'150px',u'vertical-align': u'middle', u'padding-left': u'20px', u'padding-right': u'20px',u'padding-top': u'20px', u'padding-bottom': u'20px'}, u'tagName': u'mj-image'}]

    for key,value in image[0]['attributes'].items():
        if key == "src":
            image[0]['attributes'][key] = image_pass

    finalSection['children'] = image
    output_data.append(dict(section))

    # json output file
    jsonFile = open("final.json", "w+")
    jsonFile.write(json.dumps(base))
    jsonFile.close()


# loop for image section
for key1,value1 in data1[2]['children'][1].items():
    if key1 == "name" and value1 == "image":
        link = 'https://helpx.adobe.com/in/stock/how-to/visual-reverse-image-search/_jcr_content/main-pars/image.img.jpg/visual-reverse-image-search-v2_1000x560.jpg'
        # print(link)
        imageElement(link)

# loop for text section
for key1,value1 in data1[3]['children'][1].items():
    if key1 == "characters":
        text_pass = value1
textSection(text_pass)

# loop for text section
for key1,value1 in data1[4]['children'][1].items():
    if key1 == "characters":
        text_pass = value1
textSection(text_pass)

# loop for button section
for key1,value1 in data1[5]['children'][1]['children'][1].items():
    if key1 == "characters":
        button_text = value1
buttonSection(button_text)

# loop for line element
for key1,value1 in data1[6]['children'][1].items():
    if key1 == "name" and value1 == "section7-hrline":
        lineElement()

# loop for text section
for key1,value1 in data1[7]['children'][1].items():
    if key1 == "characters":
        text_pass = value1
        # print(text_pass)
textSection(text_pass)
