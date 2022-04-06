# Google Forms Bot
This is a very simple Google Forms bot, its very barebones. It only works with forms that are open and are not limited to one response. 

Also, yes the code is prefilled with a google form link and payloads. No this is not an accident :)

## Documentation?
### target
Target is the url of the google forms, excluding the last part ("viewform", "formResponse" etc).
### payloads
This is an array of the form data. To get the key:value pairs, you can fill out the form once while having the developer tools network tab open and with preserve log enabled. After you finish the form, find all the formResponse requests and view its payload, then you can just copy the key and value from there. One of the keys is the "fbzx" value, its the long string of numbers and you can see it on the fbzx key and also the partialResponse key, for this code you just need to replace this number with "fbzx" and it will be automatically replaced with the parsed fbzx id.