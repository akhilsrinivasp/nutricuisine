<template>
    <div class="ingredient-list"> 
        <div class="ingredient-button" v-for="ingredient in ingredientsList" :key="ingredient">
            {{ ingredient }}
            <span class="material-icons remove-button" @click="removeIngredient(ingredient)">cancel</span>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'IngredientList',
        computed: {
        ingredientsList() {
                return this.$store.state.ingredients;
            }
        },
        methods: {
            removeIngredient(ingredient) {
                const index = this.$store.state.ingredients.indexOf(ingredient);
                if (index > -1) {
                    this.$store.state.ingredients.splice(index, 1);
                }
            },
        },
        created() {
            this.$store.state.ingredients = [];
        }
    }
</script>

<style scoped>
.ingredient-list {
    display: flex;
    /* have maximum 3 items in 1 row */
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    margin: 1.5% 5% 0;
    z-index: -1;
}

.ingredient-button {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 15px;
    margin: 12px;
    background-color: #f0f0f0;
    border: none;
    border-radius: 5px;
    cursor: pointer;

    transition: 1s;
    animation: reveal 0.7s forwards;
    opacity: 0;
    transform: translateX(15px);
}

@keyframes reveal {
        100% {
            opacity: 1;
            transform: translateX(0px);
        }
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