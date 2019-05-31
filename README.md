# <div align='center'>CSS Minifier</div>

A Simple Program to remove unnecessary elements from CSS Code. Written both in JavaScript and Python.

The JavaScript program is meant to be used on the web, whereas the python file is meant to be used in the backend or just as a command line utility.

## Usage

To use, clone the repo or download the Zip or just download the file you would need.

```bash
git clone https://github.com/deve-sh/CSS-Minifier.git
cd CSS-Minifier
```

### Using the JavaScript file

The JavaScript file has a `cssminifier` function that takes a CSS String as its arguments and returns its minified form.

Link the JS File to your HTML after moving the file to its directory : 

```html
<script type='text/javascript' src='./cssminifier.js'></script>
```

Then pass the CSS to it and use it whichever way you would want to.

Example :

```javascript
document.querySelector('#minified').innerText = cssminifier(document.querySelector('#unmifiedcss').innerText)
```

The JS File has a test block too for testing minification, just follow the instructions there to run them.

### Using the Python Programs

There are two Python programs : **cssminifier.py** and **minifyfile.py**. The cssminifier.py file has a function ```cssminifier``` which just like the JavaScript file takes css as its argument and returns its minified form. The program also has a Test Block at its bottom. Just follow the instructions specified there to run it.

The second file minifyfile.py is used to minify an entire css file from the command line. Just use the Python Compiler and pass the name of the file to minify. (Note : It must end with .css)

```bash
python minifyfile.py <file to minify>
```

The script will minify the css file and create a file with the same name with **-min** added to its name.

## Contribution

To contribute any feature you might like to, or make any change you deem necessary. Just make the changes to the file and start a pull request to the repo.

## Issues and Contact

For any issues, just raise an issue in the Repo.

[Contact](mailto:devesh2027@gmail.com)