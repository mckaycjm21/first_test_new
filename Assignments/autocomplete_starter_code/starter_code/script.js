let inputElement = document.querySelector('#fruit');
const suggestions = document.querySelector('.suggestions ul');

const fruit = ['Apple', 'Apricot', 'Avocado 🥑', 'Banana', 'Bilberry', 'Blackberry', 'Blackcurrant', 'Blueberry', 'Boysenberry', 'Currant', 'Cherry', 'Coconut', 'Cranberry', 'Cucumber', 'Custard apple', 'Damson', 'Date', 'Dragonfruit', 'Durian', 'Elderberry', 'Feijoa', 'Fig', 'Gooseberry', 'Grape', 'Raisin', 'Grapefruit', 'Guava', 'Honeyberry', 'Huckleberry', 'Jabuticaba', 'Jackfruit', 'Jambul', 'Juniper berry', 'Kiwifruit', 'Kumquat', 'Lemon', 'Lime', 'Loquat', 'Longan', 'Lychee', 'Mango', 'Mangosteen', 'Marionberry', 'Melon', 'Cantaloupe', 'Honeydew', 'Watermelon', 'Miracle fruit', 'Mulberry', 'Nectarine', 'Nance', 'Olive', 'Orange', 'Clementine', 'Mandarine', 'Tangerine', 'Papaya', 'Passionfruit', 'Peach', 'Pear', 'Persimmon', 'Plantain', 'Plum', 'Pineapple', 'Pomegranate', 'Pomelo', 'Quince', 'Raspberry', 'Salmonberry', 'Rambutan', 'Redcurrant', 'Salak', 'Satsuma', 'Soursop', 'Star fruit', 'Strawberry', 'Tamarillo', 'Tamarind', 'Yuzu'];

function search(str) {
	let results = [];
	if (inputElement.value){
	for (let fruitName of fruit){
		let lowerCaseFruitName = fruitName.toLowerCase();		
		if (lowerCaseFruitName.includes(str.toLowerCase())){
		results.push(fruitName);
		}
	}
	}
	else{
		results =[];
	}
	return results;
}

function searchHandler(e) {
	let results = search(inputElement.value);
	showSuggestions(results)
}

function showSuggestions(results, inputVal) {
	suggestions.innerHTML = '';
	console.log(results);
	for(let result of results) {
	const listItemElement = document.createElement('li');
	listItemElement.textContent = result;
	suggestions.appendChild(listItemElement);		
	}
}

function useSuggestion(e) {
	inputElement.value = e.target.innerHTML;
	suggestions.innerHTML = '';
}

inputElement.addEventListener('keyup', searchHandler);
suggestions.addEventListener('click', useSuggestion);
