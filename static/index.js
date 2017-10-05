function removeThis() {
	$(this).parent().hide(300);
	// $(this).parent().remove();
}

function addMore() { 
	//create a new big div first. then add a box with input field and deleteButton then appendto wrapper
 	var newDiv = document.createElement('div');
 	$(newDiv).hide();
 	var newBox = document.createElement('div');
 	
 	newBox.className = 'box';
 	newDiv.appendChild(newBox);
 	newDiv.innerHTML+= '<input class="answers" type="text" name="actors[]">';
 	
 	var deleteButton = document.createElement('div');
 	deleteButton.className = 'round-button-cancel';
 	deleteButton.onclick = removeThis;
 	deleteButton.setAttribute("title", "Remove actor");
 	deleteButton.innerHTML = '-';
 	newDiv.appendChild(deleteButton);
 	
 	document.getElementById('wrapper').appendChild(newDiv);
 	// $(newDiv).fadeIn(300);
 	$(newDiv).show(300);
}
