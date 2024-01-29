<template>
    <div class="user">
        <div class="header" v-if="show_edit_user == false">
            <div class="user-details">
                <h1 class="author">{{ user.username }}</h1>
                <p class="date">Joined {{ date_formatted }}</p>
            </div>
            <div class="edit-user">
                <button class="edit-button" @click="show_edit_user = !show_edit_user">
                <router-link id="profile" style="text-decoration: none; color: white;"
						:to="{ name: 'edit_user', params: { what: 0 } }">Edit Profile</router-link>
                    </button>
            </div>
            
        </div>
    </div>
</template>

<script>
    export default {
        name: 'UserView',
        components: {
          
        },
        data() {
            return {
                user: this.$store.state.user,
                show_edit_user: false,
            }
        },
        computed: {
            username() {
                return this.$route.params.username;
            },
            date_formatted() {
                const date = new Date(this.user.created_at);
                if (date.getDate() == new Date().getDate() - 1) {
                    return "Yesterday at " + date.toLocaleTimeString("en-US");
                }
                if (date.getDate() == new Date().getDate()) {
                    return "Today at " + date.toLocaleTimeString("en-US");
                }
                const date_formatted = date.toLocaleDateString("en-US", {month: "long", day: "numeric", year: "numeric"}) + " at " + date.toLocaleTimeString("en-US", {hour: "numeric", minute: "numeric"});
                return date_formatted;
            },
          
            is_same_user() {
                if(!this.$store.state.isLogged) return false;
                return this.$store.state.user.username == this.username
            },
        },
        methods: {
            getUser() {
                fetch(this.$store.state.url + "/user/" + this.username)
                .then(response => response.json())
                .then(data => {
                    this.user = data.user;
                })
                .catch(error => {
                    console.log(error);
                })
            },
        },
        created() {
            this.getUser();
            if(this.$store.state.isLogged)
            if(this.$store.state.user.username == this.$route.params.username)
            this.user = JSON.parse(JSON.stringify(this.$store.state.user));
            this.is_following = false;
        },
        mounted() {
        }
    }
</script>

<style scoped>
    .header {
        margin: 5%;
        padding: 5%;
        text-decoration: none;
        box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;
        border-radius: 6px;
        display: flex;
        margin-bottom: 3%;

        /* display: flex; */
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        /* margin-bottom: 2%; */
    }
    .header > div {
        display: flex;
        flex-direction: column;
    }
    .dp-image {
        width: 130px;
        height: 130px;
        border-radius: 100%;
    }
    .user-details {
        font-family: "Montserrat", sans-serif;
        font-weight: bold;
        font-size: 20px;
        color: #2c3e50;
        margin: 2% 5% 0%;
        align-items: center;
        /* text-decoration: none; */

        animation: reveal 0.7s forwards;
        opacity: 0;
        transform: translateX(-50px);
    }
    @keyframes reveal {
        100% {
            opacity: 1;
            transform: translateX(0px);
        }
    }
    .follow-user {
        margin-left: 2%;
    }
    .follow-button {
        background-color: #87CEEB;
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 10px;

        font-family: "Montserrat", sans-serif;
        font-weight: bold;
        font-size: 20px;
    }
    .unfollow-button {
        /* background-color: #87CEEB; */
        border-color: #2196F3;
        border: 4px;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 10px;

        font-family: "Montserrat", sans-serif;
        font-weight: bold;
        font-size: 20px;
    }
    .follow-button:hover {
        background-color: #2196F3;
    }
    .unfollow-button:hover {
        background-color: #2c3e50
    }
    .details {
        margin: 1% 5%;
        padding: 3% 10%;
        text-decoration: none;
        box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;
        border-radius: 6px;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 2%;
    }
    .followers {
        display: flex;
        flex-direction: column;
        align-items: center;

        font-family: "Montserrat", sans-serif;
        font-weight: bold;
        font-size: 20px;
    }
    .followers > p {
        margin: 0;
    }
    .following{
        display: flex;
        flex-direction: column;
        align-items: center;

        font-family: "Montserrat", sans-serif;
        font-weight: bold;
        font-size: 20px;
    }
    .following > p {
        margin: 0;
    }
    .public-user-name{
        font-family: "Montserrat", sans-serif;
        font-weight: bold;
        font-size: 25px;
        margin: 0;
    }
    .blog-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(600px, 1fr));
        grid-gap: 1rem;
        margin: 5%;
        margin-top: 2%;
    }
    .blog-posts {
        margin: 5%;
        padding: 5%;
        text-decoration: none;
        box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;
        border-radius: 6px;
    }
    .edit-button {
        background-color: #2c3e50;
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 10px;

        font-family: "Montserrat", sans-serif;
        font-weight: bold;
        font-size: 20px;

        animation: reveal 0.7s forwards;
        opacity: 0;
        transform: translateX(50px);
    }
    .edit-button:hover {
        background-color: #2196F3;
    }

    .edit-button:active {
        background-color: #2c3e50;
    }

    .edit-user-container {
        margin: 5%;
        padding: 5%;
        text-decoration: none;
        box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;
        border-radius: 6px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 2%;
/* 
        z-index: -1;
        position: absolute; */
    }
    .user {
        animation: reveal 0.7s forwards;
        opacity: 0;
        transform: translateY(-50px);
    }
</style>