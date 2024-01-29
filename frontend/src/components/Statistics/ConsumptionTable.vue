<template>
    <div>
        <!-- table with pagination -->
        <h2 id="message-header" style="color:#FF6347; display: none;"></h2>
        <select v-model="rowsPerPage">
            <option value="10">10</option>
            <option value="25">25</option>
            <option value="50">50</option>
            <option value="100">100</option>
        </select>

        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Calories</th>
                    <th>Carbs</th>
                    <th>Fat</th>
                    <th>Protein</th>
                    <th>Date & Time</th>
                    <th>Remove</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="food in paginatedFoods" :key="food.id">
                    <td>{{ food.name }}</td>
                    <td>{{ food.calories }}</td>
                    <td>{{ food.carbs }}</td>
                    <td>{{ food.fat }}</td>
                    <td>{{ food.protein }}</td>
                    <td>{{ food.created_at }}</td>
                    <!-- <span class="material-icons remove-button" @click="removeIngredient(ingredient)">cancel</span> -->
                    <td class="td-remove"><span class="material-icons remove-button" @click="removeFood(food)">cancel</span></td>
                </tr>
            </tbody>
        </table>

        <button @click="previousPage">Previous</button>
        <button @click="nextPage">Next</button>
        <h2 style="color:#FF6347; display: block; margin: 1.5% 0 0 0.7%; font-size: 22px;">Page {{ currentPage }} of {{ totalPages }}</h2>
        <!-- <p>Page {{ currentPage }} of {{ totalPages }}</p> -->

    </div>
</template>
<script>
export default {
    name: 'ConsumptionTable',
    data() {
        return {
            rowsPerPage: 10,
            currentPage: 1,
            foods_consumed: [],
        }
    },
    computed: {
        paginatedFoods() {
            if(this.foods_consumed.length == 0) return [];
            const startIndex = this.currentPage * this.rowsPerPage - this.rowsPerPage;
            const endIndex = startIndex + this.rowsPerPage;
            return this.foods_consumed.slice(startIndex, endIndex);
        },
        totalPages() {
            return Math.ceil(this.foods_consumed.length / this.rowsPerPage);
        }
    },
    watch: {
        rowsPerPage() {
            this.currentPage = 1;
        }
    },
    methods: {
        previousPage() {
            if (this.currentPage > 1) {
                this.currentPage--;
            }
        },
        nextPage() {
            if (this.currentPage < this.totalPages) {
                this.currentPage++;
            }
        },
        async loadConsumedFoodInfo() {
			const myHeaders = new Headers();
			myHeaders.append("Authorization", "Bearer " + this.$store.state.access_token);

			const requestOptions = {
			method: 'GET',
			headers: myHeaders,
			redirect: 'follow'
			};

			fetch(this.$store.state.url + "/consume/", requestOptions)
			.then(response => response.json())
			.then(result => {
                this.foods_consumed = result["foods"];
                // format all dates
                for(let i = 0; i < this.foods_consumed.length; i++) {
                    this.foods_consumed[i].created_at = this.dateFormatted(new Date(this.foods_consumed[i].created_at));
                }
                this.foods_consumed.reverse();
			})
			.catch(error => console.log('error', error));
		},
        async removeFood(food) {
            const food_id = food.consume_id;
            var myHeaders = new Headers();
            myHeaders.append("Authorization", "Bearer " + this.$store.state.access_token);

            var requestOptions = {
            method: 'DELETE',
            headers: myHeaders,
            redirect: 'follow'
            };

            fetch(this.$store.state.url + "/consume/" + food_id, requestOptions)
            .then(response => response.text())
            .then(result => {
                for(let i = 0; i < this.foods_consumed.length; i++) {
                    if(this.foods_consumed[i].consume_id == food_id) {
                        this.foods_consumed.splice(i, 1);
                        break;
                    }
                }
                console.log(result);
                document.getElementById('message-header').innerHTML = food.name + ' removed from List.';
                document.getElementById('message-header').style.display = 'block';
                setTimeout(() => {
                    document.getElementById('message-header').style.display = 'none';
                }, 3000);
            })
            .catch(error => console.log('error', error));
        },
        dateFormatted(date) {
            if (date.getDate() == new Date().getDate() - 1) {
                return "Yesterday at " + date.toLocaleTimeString("en-US");
            }
            if (date.getDate() == new Date().getDate()) {
                return "Today at " + date.toLocaleTimeString("en-US");
            }
            const date_formatted = date.toLocaleDateString("en-US", {month: "long", day: "numeric", year: "numeric"}) + " at " + date.toLocaleTimeString("en-US", {hour: "numeric", minute: "numeric"});
            return date_formatted;
        },
    },
    created() {
        
    },
    beforeMount() {
        this.loadConsumedFoodInfo();
    },
}
</script>
<style scoped>
/* Container styles */
div {
    margin: 2% 22%;
}

/* Table styles */
table {
    border-collapse: collapse;
    width: 90%;
    max-width: 800px; /* Adjust as needed */
    margin-bottom: 20px;
}

th, td {
    border: 1px solid #ddd;
    text-align: left;
    padding: 8px;
}

th {
    background-color: #87CEEB;
    color: white;
}

tbody tr:nth-child(odd) {
    background-color: #f2f2f2;
}

/* Select dropdown styles */
select {
    padding: 5px 10px;
    margin-bottom: 20px;
    border: 1px solid #ddd;
    border-radius: 4px;
}

/* Button styles */
button {
    font-size: 20px;
    padding: 0.75% 1.5%;
    margin: 0 2.5% 0 0;
    border: none;
    border-radius: 4px;
    background-color: #87CEEB;
    color: white;
    cursor: pointer;
    transition: background-color 0.3s;
}

button:hover {
    background-color: #5c9cb3;
}

button:disabled {
    background-color: #ccc;
    cursor: default;
}

/* Page number display */
p {
    margin-top: 15px;
}

.remove-button {
    margin-left: 10px;
    border: none;
    background-color: transparent;
    cursor: pointer;
    color: #FF7F50;
    opacity: 75%;
    transition: 1s;
    border-radius: 100%;
}

.remove-button:hover {
    color: #FFF;
    background-color:#FF6347;
}
</style>
