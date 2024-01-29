<template>
	<div class="master">
		<nav class="navbar navbar-expand-lg navbar-light">
			<div class="navbar-brand">
				<div class="on-left">
					<router-link class="elements" style="font-size: 30px;" to="/">NutriCuisine</router-link>
				</div>
				<div class="on-right">
					<router-link class="elements" v-if="!isLogged" to="/login">Login</router-link>
					<router-link class="elements" v-if="!isLogged" to="/signup">Sign Up</router-link>
					<router-link class="elements" v-if="isLogged" to="/recommend/recipe">Curate</router-link>
					<router-link class="elements" v-if="isLogged" to="/consumption/statistics">Stats</router-link>
					<router-link class="elements" v-if="isLogged" to="/profile">Profile</router-link>
					<router-link class="elements" v-if="isLogged" to="/logout">Logout</router-link>
				</div>
			</div>
		</nav>
		<router-view />
	</div>
	
</template>

<script>

export default {
	name: 'App',
	data() {
		return {
			msg: 'Welcome to Your Vue.js App'
		}
	},
	components: {
		
	},
	methods: {
	},
	computed: {
		isLogged() {
			return this.$store.state.access_token === "null" ? false : true;
		},
		profile() {
			const image_url = this.$store.state.url + "/image/" + "account.png";
			return image_url;
		},
		upload_icon() {
			const image_url = this.$store.state.url + "/image/" + "upload.png";
			return image_url;
		},
	},
	created() {
		
	},
	mounted() {
		console.log(this.$store.state.access_token === "null")
	},
}
</script>

<style scoped>
#app {
	font-family: "Montserrat", sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	color: #2c3e50;
}

h1,
h2,
h3 {
	font-weight: normal;
	font-family: "Montserrat";
}

nav {
	padding: 0.5% 2%;
	
}

nav a {
	font-weight: bold;
	color: #2c3e50;
}

nav a.router-link-exact-active {
	color: #FF7F50;
}

.navbar-brand {
	display: flex;
	justify-content: space-between;
	align-items: center;
}

.navbar-brand .on-left {
	justify-content: left;
	align-items: center;
}

.navbar-brand .on-right {
	justify-content: right;
	align-items: center;
}

.on-right {
	display: flex;
	justify-content: space-between;
	align-items: right;
	padding: 1.75% 0 0 ;
}

.elements {
	margin: 0 10px;
	text-decoration: none;
	opacity: 0;
	transition: 0.5s;
	animation: reveal 1s forwards;
	transform: translateX(50px);
}

@keyframes reveal {
	100% {
		opacity: 1;
		transform: translateX(0px);
	}
}

.elements:hover {
	color: #FF7F50;
}

.dropdown:hover>.dropdown-menu {
	margin-top: 20px;
	display: block;
	animation: dropdown-animation 0.3s ease;
}

@keyframes dropdown-animation {
	0% {
		opacity: 0;
	}

	100% {
		opacity: 1;
	}
}

.dropdown-combined {
	border-radius: 5;
	padding: 0.2%;
}

.dropdown-combined .dropdown-toggle::after {
	display: none;
}

.dropdown-menu {
	width: 200px;
}

</style>
