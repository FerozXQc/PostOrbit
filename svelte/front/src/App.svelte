<script>
// import Header from './lib/header.svelte'
const BaseUrl = 'http://localhost:8000'
let name='feroz'
let password='123'

const login = async() =>{
    const res = await fetch(`${BaseUrl}/login`,{
        method:'POST',
        headers:{'Content-Type':'application/x-www-form-urlencoded'},
        body: new URLSearchParams({name,password}),
        credentials:'include'
    });
    const data= await res.json();
    console.log(data)
}

login()

</script>

<main>
<!-- <Header/> -->
</main>