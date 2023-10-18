const $picHolder = $("#pic-holder");
const $searchBox = $("#search-box");

function makeGif(results) {
    let nResults = results.data.length;
    if (nResults) {
      let random = Math.floor(Math.random() * nResults);
      let $newDiv = $("<div>",);
      let $newImg = $("<img>", {
        src: results.data[random].images.original.url,
      });
      $newDiv.append($newImg);
      $picHolder.append($newDiv);
    }
  }
$("form").on("submit", async function(e){
    e.preventDefault();
    let $searchBoxValue = $searchBox.val();
    $searchBox.val("");

    const result = await axios.get("http://api.giphy.com/v1/gifs/search", {
        params:{
            q: $searchBoxValue,
            api_key: "CZjN2D1T8SSHpxo8FeYbre8ev1DZ4WSA"
        }
        });
    console.log($searchBoxValue);
    makeGif(result.data);

})