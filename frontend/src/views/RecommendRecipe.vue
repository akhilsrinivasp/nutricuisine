<template>
    <div class="recommend-recipe">
        <div class="section-1" v-if="!consumed">
            <h1>What do you have ??</h1>
            <PredictImage />
            <div style="z-index: 1000; position: relative;">
                <DropdownSearch />
            </div>
            <div style="z-index: 1; position: relative;">
                <IngredientList />
            </div>
        </div>
        <div class="section-2" v-if="len_ing_g_0">
            <GenerateRecipe />
        </div>
    </div>
</template>

<script>
import PredictImage from '@/components/Curate/PredictImage.vue';
import IngredientList from '@/components/Curate/IngredientList.vue';
import DropdownSearch from '@/components/Curate/DropdownSearch.vue';
import GenerateRecipe from '@/components/Curate/GenerateRecipe.vue';

export default {
    name: 'RecommendRecipe',
    components: {
        PredictImage,
        IngredientList,
        DropdownSearch,
        GenerateRecipe,
    },

    computed: {
        len_ing_g_0() {
            return this.$store.state.ingredients.length > 0;
        },
        consumed() {
            return this.$store.state.consumed;
        }
    },

    beforeUnmount() {
        this.$store.state.ingredients = [];
    },
}
</script>

<style scoped>
.recommend-recipe {
    padding: 5% 10% 10%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
}

.section-1 {
    margin: 0 0% 5%;
    padding: 6% 0% 5%;
    text-decoration: none;
    box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;
    border-radius: 10px;
    width:75%;
    animation: reveal 0.7s forwards;
    opacity: 0;
    transform: translateY(-15px);
}

.section-2 {
    margin: 0 0% 5%;
    padding: 6% 0% 5%;
    text-decoration: none;
    box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;
    border-radius: 10px;
    width:75%;
    animation: reveal 0.7s forwards;
    opacity: 0;
    transform: translateY(-15px);
}

h1 {
    font-family: "Montserrat", sans-serif;
    font-size: 40px;
    color: #87CEEB;
    margin: 0 1% 4%;
    margin-left: 0;
    font-weight: bold;
    text-align: center;
}

@keyframes reveal {
        100% {
            opacity: 1;
            transform: translateY(0px);
        }
    }
</style>
