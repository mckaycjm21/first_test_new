"use strict";

const $showsList = $("#showsList");
const $episodesArea = $("#episodesArea");
const $episodesList = $("#episodesList");
const $searchForm = $("#searchForm");


/** Given a search term, search for tv shows that match that query.
 *
 *  Returns (promise) array of show objects: [show, show, ...].
 *    Each show object should contain exactly: {id, name, summary, image}
 *    (if no image URL given by API, put in a default image URL)
 */

async function getShowsByTerm(searchTerm) {
  // ADD: Remove placeholder & make request to TVMaze search shows API.

  const result = await axios.get(`https://api.tvmaze.com/search/shows?q=${searchTerm}`,);
  return result.data.map(results => {
    const show = results.show;
    return{
    id: show.id,
    name: show.name,
    summary: show.summary,
    image: show.image ? show.image.medium : "https://t3.ftcdn.net/jpg/04/34/72/82/240_F_434728286_OWQQvAFoXZLdGHlObozsolNeuSxhpr84.jpg"
    };
  });
}


/** Given list of shows, create markup for each and to DOM */

function populateShows(shows) {
  $showsList.empty();

  for (let show of shows) {
    const $show = $(
      `<div data-show-id="${show.id}" class="Show col-md-12 col-lg-6 mb-4">
         <div class="media">
           <img
              src="${show.image}"
              alt="https://www.rd.com/wp-content/uploads/2021/03/GettyImages-1133605325-scaled-e1617227898456.jpg?fit=696%2C463?fit=700,700https://www.rd.com/wp-content/uploads/2021/03/GettyImages-1133605325-scaled-e1617227898456.jpg?fit=696%2C463?fit=700,700"
              class="w-25 me-3">
           <div class="media-body">
             <h5 class="text-primary">${show.name}</h5>
             <div><small>${show.summary}</small></div>
             <button class="btn btn-outline-light btn-sm Show-getEpisodes">
               Episodes
             </button>
           </div>
         </div>
       </div>
      `);

    $showsList.append($show);
  }
}


/** Handle search form submission: get shows from API and display.
 *    Hide episodes area (that only gets shown if they ask for episodes)
 */

async function searchForShowAndDisplay() {
  const term = $("#searchForm-term").val();
  const shows = await getShowsByTerm(term);

  $episodesArea.hide();
  populateShows(shows);
}

$searchForm.on("submit", async function (evt) {
  evt.preventDefault();
  await searchForShowAndDisplay();
});


/** Given a show ID, get from API and return (promise) array of episodes:
 *      { id, name, season, number }
 */

async function getEpisodesOfShow(id) {
  const epResult = await axios.get(`https://api.tvmaze.com/shows/${id}/episodes`,);

  return epResult.data.map(ep => ({
    id : ep.id,
    name : ep.name,
    season : ep.season,
    number : ep.number
    }));
  }
 

/** Write a clear docstring for this function... */

function populateEpisodes(episodes) { 
  $episodesList.empty();

  for (let episode of episodes) {
    const $episode = $(
      `<li>
        ${episode.name}: 
      (season ${episode.season}, episode ${episode.number})
      </li>`
      );

    $episodesList.append($episode);
  }
  $episodesArea.show();
}
async function getEpisodesAndDisplay(evt) {
  const showId = evt.target.closest(".Show").getAttribute(`data-show-id`);
  const episodes = await getEpisodesOfShow(showId);
  console.log(episodes)
  populateEpisodes(episodes);
}
$showsList.on("click", ".Show-getEpisodes", getEpisodesAndDisplay); 
