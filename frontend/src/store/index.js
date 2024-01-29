import { createStore } from 'vuex'

export default createStore({
	state: {
		access_token: localStorage.getItem('access_token') || null,
		refresh_token: localStorage.getItem('refresh_token') || null,
		user: JSON.parse(localStorage.getItem('user')) || null,
		isLogged: localStorage.getItem('access_token') || null,
		url: "http://127.0.0.1:5051/",
		
		ingredients: [],
		consumed: false,
	},
	getters: {
	},
	mutations: {
		setUser(state, user) {
			state.user = user
			localStorage.setItem('user', JSON.stringify(user))
		},
		setTokens(state, tokens) {
			state.access_token = tokens.access_token
			state.refresh_token = tokens.refresh_token
			state.isLogged = true
			localStorage.setItem('access_token', tokens.access_token)
			localStorage.setItem('refresh_token', tokens.refresh_token)
			localStorage.setItem('isLogged', true)
		},
	},
	actions: {
		async login({ commit }, user) {
			// convert to form data
			const user_form_data = new FormData()
			user_form_data.append('username', user.username)
			user_form_data.append('password', user.password)
			const requestOptions = {
				method: 'POST',
				body: user_form_data,
				redirect: 'follow'
			};
			const response = await fetch(this.state.url + 'auth/login', requestOptions)
			if (!response.ok) {
				this.$router.push('/');
			}
			const data = await response.json()
			commit('setTokens', data)
			const response2 = await fetch(this.state.url + 'auth/get_user',
				{
					method: 'GET',
					headers: {
						'Content-Type': 'application/json',
						'Authorization': 'Bearer ' + this.state.access_token
					}
				})
			const data2 = await response2.json()
			commit('setUser', data2)
		},
		async refresh({ commit }) {
			const response = await fetch(this.state.url + 'refresh',
				{
					method: 'POST',
					headers: {
						'Content-Type': 'application/json',
						'Authorization': 'Bearer ' + this.state.refresh_token
					},
				})
			// if error then return 
			if (!response.ok) {
				this.state.isLogged = false
				localStorage.setItem('isLogged', false)
				return
			}
			const data = await response.json()
			commit('setTokens', data)
		},
		logout({ commit }) {
			this.state.isLogged = false
			// remove isLogged
			localStorage.removeItem('isLogged')
			localStorage.setItem('access_token', null)
			localStorage.setItem('refresh_token', null)
			localStorage.setItem('user', null)

			const token = {
				access_token: null,
				refresh_token: null
			}
			commit('setTokens', token)
			commit('setUser', null)
		},
		async uploadImage({ commit }, image) {
			const fData = new FormData()
			let type = 'dp';
			let image_returned = ''
			console.log(type)
			fData.append('image', image)
			fData.append('type', type)
			await fetch(this.state.url + 'image', {
				method: 'POST',
				headers: {
					'Authorization': 'Bearer ' + this.state.access_token,
				},
				body: fData
			})
				.then(response => response.json())
				.then(data => {
					image_returned = data.image_name
				})
			commit('setImage', image_returned)
			return image_returned
		},
		async reloadUser({ commit }, username) {
			await fetch(this.$store.state.url + "/user/" + username)
				.then(response => response.json())
				.then(data => {
					commit('setUser', data)
				})
				.catch(error => {
					console.log(error);
				})
		},
		
	},
})
