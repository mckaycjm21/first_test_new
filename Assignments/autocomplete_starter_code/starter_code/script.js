let input = document.querySelector('#fruit');
const suggestions = document.querySelector('.suggestions ul');
let makeLi  = document.createElement("li");
let permList = [];


const fruit = ['Apple', 'Apricot', 'Avocado 🥑', 'Banana', 'Bilberry', 'Blackberry', 'Blackcurrant', 'Blueberry', 'Boysenberry', 'Currant', 'Cherry', 'Coconut', 'Cranberry', 'Cucumber', 'Custard apple', 'Damson', 'Date', 'Dragonfruit', 'Durian', 'Elderberry', 'Feijoa', 'Fig', 'Gooseberry', 'Grape', 'Raisin', 'Grapefruit', 'Guava', 'Honeyberry', 'Huckleberry', 'Jabuticaba', 'Jackfruit', 'Jambul', 'Juniper berry', 'Kiwifruit', 'Kumquat', 'Lemon', 'Lime', 'Loquat', 'Longan', 'Lychee', 'Mango', 'Mangosteen', 'Marionberry', 'Melon', 'Cantaloupe', 'Honeydew', 'Watermelon', 'Miracle fruit', 'Mulberry', 'Nectarine', 'Nance', 'Olive', 'Orange', 'Clementine', 'Mandarine', 'Tangerine', 'Papaya', 'Passionfruit', 'Peach', 'Pear', 'Persimmon', 'Plantain', 'Plum', 'Pineapple', 'Pomegranate', 'Pomelo', 'Quince', 'Raspberry', 'Salmonberry', 'Rambutan', 'Redcurrant', 'Salak', 'Satsuma', 'Soursop', 'Star fruit', 'Strawberry', 'Tamarillo', 'Tamarind', 'Yuzu'];

function search(str) {
	let results = [];
	let lowerCaseChar = "";
	let userInputHere = ""
	for(let i = 0; i < str.length; i++){
		lowerCaseChar = str.toLowerCase();
		userInputHere[i] = lowerCaseChar;
		console.log(userInputHere);
	}
	for (let test of fruit){
		let lowerCaseFruit = test.toLowerCase();
		if (lowerCaseFruit.includes(lowerCaseChar)){
			results.push(lowerCaseFruit);
		}
	}

	return results;
}

function searchHandler(e) {
	let results = search(input.value);
	console.log(results);
}

function showSuggestions(results, inputVal) {
	//Take the Array from search handler and return an 
}

function useSuggestion(e) {
	// onMouseClick input value from li into search text box value
}

input.addEventListener('keyup', searchHandler);
suggestions.addEventListener('click', useSuggestion);
