async function getAllCupcakes(){
    let response = await axios.get("/api/cupcakes") 
    for (let key in response.data){
        console.log(response.data[key].flavor)
        $('table').append(`
        <tr>
            <td>${response.data[key].flavor} - <a href="#" class="btn btn-danger btn-sm" onclick="deleteCupcake(${response.data[key].id})">Delete<a></td>
            <td>${response.data[key].rating}</td>
            <td>${response.data[key].size}</td>
        </tr>`)

    }

}
getAllCupcakes();

$('.add_cupcake').click(function() {
    flavor = $('#flavor').val();
    size = $('#size').val();
    rating = $('#rating').val();
    image = $('#image').val();
    alert(flavor + size + rating + image);
    axios.post('/api/cupcakes', {   flavor: flavor,
                                    size: size,
                                    rating: rating,
                                    image: image})
});

function deleteCupcake(id){
    axios.delete(`/api/cupcakes/${id}`)
    location.reload()
}