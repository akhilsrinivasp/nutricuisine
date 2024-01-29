<template>
    <div class = "home">
        <div class="header">
            <h1 class="animate1">A Food Curating Platform</h1>
            <p class="animate2">Welcome to the place where <span style="color:#FF7F50">culinary enthusiasts</span> and food lovers unite to explore, discover, and <span style="color:#FF7F50">celebrate</span> the diverse world of gastronomy. Whether you're a seasoned chef, an amateur cook, or simply someone who relishes savoring delectable dishes, our platform is designed to <span style="color:#FF7F50">enhance your food journey</span> in more ways than one.</p>
        </div>
        <img class="image animate3" :src="require('../assets/homepage_1.jpg')" alt="homepage_1">
    </div>
</template>

<script>

    export default {
        name: 'HomeView',
        components: {
           
        },
        created() {
        }
    }
</script>

<style scoped>
    .home {
        margin: 0;
        padding: 4%;
        padding-top: 0;
        display: flex;
        
    }
    .image {
        width: 200%;
        height: 200%;
        margin: 5%;
        margin-right: 14%;
        margin-top: 5%;
        border-radius: 6px;
    }
    .header {
        margin: 5%;
        margin-bottom: 2%;
        padding: 5%;
        text-decoration: none;
        /* box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset; */
        border-radius: 6px;
    }

    h1 {
        font-family: "Montserrat", sans-serif;
        font-weight: bold;
        font-size: 50px;
        color: #87CEEB;
    }
    p {
        font-family: "Montserrat", sans-serif;
        font-size: 22px;
        color: #2c3e50;
        line-height: 1.75;
    }

    .blog-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(600px, 1fr));
        grid-gap: 1rem;
        margin: 5%;
        margin-top: 0;
    }

    .blog-posts {
        margin: 5%;
        padding: 5%;
        text-decoration: none;
        box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;
        border-radius: 6px;
    }
    
    @media screen and (max-width: 768px) {
        .blog-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            grid-gap: 1rem;
            margin: 5%;
        }
    }

    .animate1 {
        animation: reveal 1s forwards;
        opacity: 0;
        transform: translateX(-100px);
    }
    
    .animate2 {
        animation: reveal 1s forwards;
        opacity: 0;
        transform: translateX(100px);
    }
     
    .animate3 {
        animation: reveal 1s forwards;
        opacity: 0;
        transform: translateY(100px);
    }

    @keyframes reveal {
        100% {
            opacity: 1;
            transform: translateX(0px);
        }
    }
    
</style>