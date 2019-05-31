/*
	A simple CSS Minifier
*/

// Main function to minify CSS.

function cssminifier(css = ""){
	// Checking for the right type of argument.

	if (typeof css !== "string"){
		throw new Error("Invalid Type Passed.");
	}

	// Required Variables

	let minifiedcss = ``,
		inComment = false,
		spaceregex = /^[\s{}:]$/;

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