# figma json to mjml json
1) Open the figma design and change the button text.
2) Run python file run.py to get fout.json file containing the layer details in json format.
    python3 run.py
3) Then run run-test.py which change the base output file base1output.json which makes button with the text you had changed earlier. 
    python3 run-test.py
4) Json2mjml tool can change json to mjml and mjml cli tool can change mjml into the responsive html. Just for the test you can paste json code to this
  link :https://codepen.io/briancsinger/pen/rpYxRJ to get instance output of html.

