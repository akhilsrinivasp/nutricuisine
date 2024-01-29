<template>
    <div class="generate-recipe-container">
        <h1 v-if="!recipe">Let's Make you Something !</h1>
        <button v-if="!recipe" @click="fetchRecipe" class="generate-button">Generate Recipe</button>
        <div v-if="recipe" class="recipe-content">
            <h1>{{ recipe.recipe.title }}</h1>
            <div class="food-info">
                <div class="food-sub-info">
                    <p class="food-sub-info-num">{{ recipe.recipe.servings }}<span style="font-size: 15px; padding: 3px 0px 0px 3px;">P</span></p>
                    <p class="food-sub-info-tag">Servings</p>
                </div>
                <div class="food-sub-info">
                    <p class="food-sub-info-num">{{ recipe.recipe.calories }} <span style="font-size: 15px; padding: 3px 0px 0px 3px;">kcal</span></p>
                    <p class="food-sub-info-tag">Calories</p>
                </div>
                <div class="food-sub-info">
                    <p class="food-sub-info-num">{{ recipe.recipe.carbs }} <span style="font-size: 15px; padding: 3px 0px 0px 3px;">g</span></p>
                    <p class="food-sub-info-tag">Carbs</p>
                </div>
                <div class="food-sub-info">
                    <p class="food-sub-info-num">{{ recipe.recipe.fat }} <span style="font-size: 15px; padding: 3px 0px 0px 3px;">g</span></p>
                    <p class="food-sub-info-tag">Fat</p>
                </div>
                <div class="food-sub-info">
                    <p class="food-sub-info-num">{{ recipe.recipe.protein }} <span style="font-size: 15px; padding: 3px 0px 0px 3px;">g</span></p>
                    <p class="food-sub-info-tag">Protein</p>
                </div>
            </div>
            <h2>Ingredients</h2>
            <ul class="ingredients-list">
                <li class="ingredient" v-for="ingredient in recipe.recipe.ingredients" :key="ingredient">{{ ingredient }}</li>
            </ul>
            <h2>Instructions</h2>
            <ol class="instructions-list">
                <li class="instruction" v-for="instruction in recipe.recipe.instructions" :key="instruction">{{ instruction }}</li>
            </ol>
        </div>
        <div class="confirmation-section" v-if="recipe">
            <button v-if="!consumed" @click="fetchRecipeAgain" class="generate-again-button">Anything Else in There?</button>
            <button v-if="!consumed" @click="fetchConsumeFood" class="consume-button">Looks Yummy!</button>
        </div>
        <h2 id="consumed-successfully" style="color:#FF6347; display: none;">Item has been added to your list of food consumed.</h2>
    </div>
</template>

<script>
export default {
    name: 'GenerateRecipe',
    data() {
        return {
            recipe: null,
        }
    },
    computed: {
        consumed() {
            return this.$store.state.consumed;
        }
    },
    methods: {
        async fetchRecipe() {
            window.scrollTo(0,document.body.scrollHeight);

            // Change the button to loading
            const button = document.querySelector('.generate-button');
            button.innerHTML = 'Loading...';
            button.style.backgroundColor = '#fe8a75';
            button.disabled = true;
            
            var formdata = new FormData();
            let ingredients = this.$store.state.ingredients;
            ingredients = ingredients.join(', '); 
            formdata.append("ingredients", ingredients);

            var requestOptions = {
            method: 'POST',
            body: formdata,
            redirect: 'follow'
            };
            fetch(this.$store.state.url + 'recommend', requestOptions)
            .then(response => response.json())
            .then(data => {
                console.log(data);
                this.recipe = data;
                button.innerHTML = 'Generate Recipe';
            })
            .catch(error => {
                console.error(error);
                button.innerHTML = 'Generate Recipe';
            });
        },
        async fetchRecipeAgain() {
            window.scrollTo(0,document.body.scrollHeight);

            // Change the button to loading
            const button = document.querySelector('.generate-again-button');
            button.innerHTML = 'Loading...';
            button.style.backgroundColor = '#fe8a75';
            
            var formdata = new FormData();
            let ingredients = this.$store.state.ingredients;
            ingredients = ingredients.join(', '); 
            formdata.append("ingredients", ingredients);

            var requestOptions = {
            method: 'POST',
            body: formdata,
            redirect: 'follow'
            };
            fetch(this.$store.state.url + 'recommend', requestOptions)
            .then(response => response.json())
            .then(data => {
                console.log(data);
                this.recipe = data;
                button.innerHTML = 'Anything Else in There?';
            })
            .catch(error => {
                console.error(error);
                button.innerHTML = 'Anything Else in There?';
            });
        },
        async fetchConsumeFood() {
            var myHeaders = new Headers();
            myHeaders.append("Authorization", "Bearer " + this.$store.state.access_token);

            var formdata = new FormData();
            formdata.append("food_id", this.recipe.recipe.id);
            formdata.append("quantity", "1");

            var requestOptions = {
            method: 'POST',
            headers: myHeaders,
            body: formdata,
            redirect: 'follow'
            };

            fetch(this.$store.state.url + "/consume/", requestOptions)
            .then(response => response.json())
            .then(result => {
                console.log(result);
                this.$store.state.consumed = true;
                setTimeout(() => {
                    document.getElementById('consumed-successfully').style.display = 'block';
                }, 0);
                
                setTimeout(() => {
                    document.getElementById('consumed-successfully').style.display = 'none';
                }, 3000);
            })
            .catch(error => console.log('error', error));
           
        }
    },
    beforeUnmount() {
        this.$store.state.consumed = false;
    }
}
</script>

<style scoped>
.generate-recipe-container {
    display: flex;
    justify-content: center; 
    align-items: center; 
    height: 100%; 
    flex-direction: column;
}

.food-info {
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
}
.food-sub-info {
    margin: 0 2%;
    padding: 1%;
}
.food-sub-info-num {
    font-size: 20px;
    font-weight: 600;
    background-color: #FF6347;
    color: aliceblue;
    width: 90px;
    height: 90px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 100%;

    animation: reveal 1s forwards;
    opacity: 0;
    transform: translateX(-25px);
}
.food-sub-info-tag {
    font-size: 20px;
    font-weight: 700;
    color: #87CEEB;
    margin-top:0;

    animation: reveal 1s forwards;
    opacity: 0;
    transform: translateX(-25px);
}
.generate-button {
    padding: 10px 20px;
    
    border: none;
    border-radius: 5px;
    font-size: 20px;
    cursor: pointer;
    transition: background-color 0.3s;

    background-color: #FF6347;
    color:aliceblue;

    animation: reveal 0.7s forwards;
    opacity: 0;
    transform: translateY(-25px);
}

.generate-button:hover {
    background-color: #b12d16;
    color:aliceblue;
}

.ingredients-list {
    margin: 0 20% 4%;
    padding: 0 5%;
    list-style-type:square;
    font-size: 21px;
    font-weight: 500;
}

.ingredient {
    padding: 0.7% 0;
    animation: reveal 0.7s forwards;
    opacity: 0;
    transform: translateY(-25px);
}

.instructions-list {
    margin: 0 14% 4% 20%;
    padding: 0 5%;
    list-style-type:decimal;
    font-size: 21px;
    font-weight: 500;
}

.instruction {
    padding: 0.7% 0;

    animation: reveal 0.7s forwards;
    opacity: 0;
    transform: translateY(-25px);
}

h1 {
    font-family: "Montserrat", sans-serif;
    font-size: 40px;
    color: #87CEEB;
    margin: 0 1% 4%;
    margin-left: 0;
    font-weight: bold;
    text-align: center;
    animation: reveal 0.7s forwards;
    opacity: 0;
    transform: translateY(25px);
}

h2 {
    font-family: "Montserrat", sans-serif;
    font-size: 28px;
    color: #87CEEB;
    margin: 1.5% 1% 2%;
    margin-left: 0;
    font-weight: bold;
    text-align: center;

    animation: reveal 0.7s forwards;
    opacity: 0;
    transform: translateY(25px);
}

@keyframes reveal {
    100% {
        opacity: 1;
        transform: translateY(0px) translateX(0px);
    }
}

.confirmation-section {
    display: flex;
    margin: 0;
    width: 100%;
    align-items:space-between;
    justify-content: center;
}

.generate-again-button {
    padding: 1.5% 2%;
    margin: 0 6% 0 0;
    
    border: none;
    border-radius: 5px;
    font-size: 20px;
    cursor: pointer;
    transition: background-color 0.3s;

    background-color: #FF6347;
    color:aliceblue;

    animation: reveal 0.7s forwards;
    opacity: 0;
    transform: translateY(-25px);
}
.generate-again-button:hover {
    background-color: #b12d16;
    color:aliceblue;
}

.consume-button {
    padding: 1.5% 2%;
    
    border: none;
    border-radius: 5px;
    font-size: 20px;
    cursor: pointer;
    transition: background-color 0.3s;

    background-color: #87CEEB;
    color:aliceblue;

    animation: reveal 0.7s forwards;
    opacity: 0;
    transform: translateY(-25px);
}
.consume-button:hover {
    background-color: #5c9cb3;
    color:aliceblue;
}

.consumed-successfully {
    transition: 1s;
    animation: reveal 0.7s forwards;
    opacity: 0;
    transform: translateY(-25px);
}
</style>
