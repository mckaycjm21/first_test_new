async function createUser(){
let newUserInfo = await axios.post(`https://hack-or-snooze-v3.herokuapp.com/signup`, {
        "user": {
            "name": "Test User978979121",
            "username": "test876789122",
            "password": "password"
        }
})
.then((response) => console.log(response.data))
.then((error) => console.log(error));
}
async function getUser(){
    let user = await axios.get(`https://hack-or-snooze-v3.herokuapp.com/users/test876789122?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3Q4NzY3ODkxMjIiLCJpYXQiOjE2OTc4NDM3NTV9.X6Agzkpn8gUP1pau5WXiv3euzKfYvsKwbq2Zak9jgAE`)
console.log(user.data.user.name);

}

async function deleteUser(){
    let dUser = await axios.delete('https://hack-or-snooze-v3.herokuapp.com/users/test876789122?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3Q4NzY3ODkxMjIiLCJpYXQiOjE2OTc4NDU2OTB9.1ENSxS0u9NVo9aJ3TFa7m8ZrhRahdwlUCp6cfblaefw',
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3Q4NzY3ODkxMjIiLCJpYXQiOjE2OTc4NDU2OTB9.1ENSxS0u9NVo9aJ3TFa7m8ZrhRahdwlUCp6cfblaefw"
})
console.log(dUser);
}