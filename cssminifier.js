/*
	A simple CSS Minifier.
	
	Author : Devesh Kumar.

	Process : 
	---------

	1. Get the CSS.
	2. Iterate over it character by character.
	3. Check if we are inside a comment. If yes, no need to add any characters inside the comment.
	4. If not, check if the character is a line break or an unnecessary whitespace. If yes, don't add it.
	5. If not, add the character to the minified css.
	6. Return the Minified CSS.
*/

// Main function to minify CSS.

function cssminifier(css = ""){
	// Checking for the right type of argument.

	if (typeof css !== "string"){
		throw new Error("Invalid Type Passed.");
	}

	// Required Variables

	let minifiedcss = ``,			// The string that will later be the minified css.
		inComment = false,			// Variable to keep track whether the iterator is part of a comment.
		spaceregex = /^[\s{}:]$/;	// Regex to check whether the character next to the current character is a punctuation mark and hence, doesn't need to be added.

	for(let char = 0; char < css.length; char++){
		// Iterating over the css char by char.

		if(inComment === false){
			if(css[char] === '\n'){
				// Removing line breaks.
				continue;
			}
			else if(css[char] === '/' && css[char + 1] === '*'){
				// Start of a comment.
				inComment = true;	// We are inside a comment. Don't add anything unless it gets over.
				char++;				// No need to evaluate next character.
				continue;
			}
			else if(/\s/.test(css[char]) && (spaceregex.test(css[char + 1]) || spaceregex.test(css[char - 1]))){
				// Remove all the extra whitespaces.
				continue;
			}

			minifiedcss += css[char];
		}
		else{
			// If we are inside a comment. We don't need to add anything.
			// We just need to check if the comment has ended or not.

			if(css[char] === '*' && css[char + 1] === '/'){
				inComment = false;	// No longer inside a comment.
				char++;		// No need to evaluate next character.
				continue;
			}
			else{
				continue;	// Don't add the character as its inside a comment.
			}
		}
	}

	// Now removing all the instances where a closing bracket (}) comes after a semicolon as that isn't needed.

	minifiedcss = [...minifiedcss];	 // Turning the string into an array of characters.

	for(let char = 0; char < minifiedcss.length; char++){
		if(minifiedcss[char] === ';' && minifiedcss[char + 1] === '}'){
			minifiedcss[char] = '';	// No data in the character now.
		}
	}

	minifiedcss = minifiedcss.join('');	// Joining the array back to a string.

	return minifiedcss;
}