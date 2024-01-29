<template>
    <div class="search-functionality">
        <input 
            class="form-control"
            type="text" 
            v-model="searchQuery" 
            @input="performSearch" 
            @keydown.down.prevent="navigateResults('down')"
            @keydown.up.prevent="navigateResults('up')"
            @keydown.enter.prevent="addIngredient"
            @keydown.esc="clearSearchResults"
            placeholder="Broccoli..."
        />
        <div v-if="searchResults.length" class="results-dropdown">
            <div 
                v-for="(result, index) in searchResults" 
                :key="result"
                :class="{'highlighted': index === highlightedIndex}"
                @click="addIngredient(result)"
                @mouseover="highlightedIndex = index"
            >
                {{ result }}
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: 'DropdownSearch',
    data() {
        return {
            searchQuery: '',
            searchResults: [],
            highlightedIndex: -1,
            listOfAvailableIngredients: {
                "fruits": [
                    "apple",
                    "apricot",
                    "avocado",
                    "banana",
                    "bell pepper",
                    "bilberry",
                    "blackberry",
                    "blackcurrant",
                    "blood orange",
                    "blueberry",
                    "boysenberry",
                    "breadfruit",
                    "canary melon",
                    "cantaloupe",
                    "cherimoya",
                    "cherry",
                    "chili pepper",
                    "clementine",
                    "cloudberry",
                    "coconut",
                    "cranberry",
                    "cucumber",
                    "currant",
                    "damson",
                    "date",
                    "dragonfruit",
                    "durian",
                    "eggplant",
                    "elderberry",
                    "feijoa",
                    "fig",
                    "goji berry",
                    "gooseberry",
                    "grape",
                    "grapefruit",
                    "guava",
                    "honeydew",
                    "huckleberry",
                    "jackfruit",
                    "jambul",
                    "jujube",
                    "kiwi fruit",
                    "kumquat",
                    "lemon",
                    "lime",
                    "loquat",
                    "lychee",
                    "mandarine",
                    "mango",
                    "mulberry",
                    "nectarine",
                    "nut",
                    "olive",
                    "orange",
                    "papaya",
                    "passionfruit",
                    "peach",
                    "pear",
                    "persimmon",
                    "physalis",
                    "pineapple",
                    "plum",
                    "pomegranate",
                    "pomelo",
                    "purple mangosteen",
                    "quince",
                    "raisin",
                    "rambutan",
                    "raspberry",
                    "redcurrant",
                    "rock melon",
                    "salal berry",
                    "satsuma",
                    "star fruit",
                    "strawberry",
                    "tamarillo",
                    "tangerine",
                    "tomato",
                    "ugli fruit",
                    "watermelon"
                ],
                "vegetables": [
                    "acorn squash",
                    "alfalfa sprout",
                    "amaranth",
                    "anise",
                    "artichoke",
                    "arugula",
                    "asparagus",
                    "aubergine",
                    "azuki bean",
                    "banana squash",
                    "basil",
                    "bean sprout",
                    "beet",
                    "black bean",
                    "black-eyed pea",
                    "bok choy",
                    "borlotti bean",
                    "broad beans",
                    "broccoflower",
                    "broccoli",
                    "brussels sprout",
                    "butternut squash",
                    "cabbage",
                    "calabrese",
                    "caraway",
                    "carrot",
                    "cauliflower",
                    "cayenne pepper",
                    "celeriac",
                    "celery",
                    "chamomile",
                    "chard",
                    "chayote",
                    "chickpea",
                    "chives",
                    "cilantro",
                    "collard green",
                    "corn",
                    "corn salad",
                    "courgette",
                    "cucumber",
                    "daikon",
                    "delicata",
                    "dill",
                    "eggplant",
                    "endive",
                    "fennel",
                    "fiddlehead",
                    "frisee",
                    "garlic",
                    "gem squash",
                    "ginger",
                    "green bean",
                    "green pepper",
                    "habanero",
                    "herbs and spice",
                    "horseradish",
                    "hubbard squash",
                    "jalapeno",
                    "jerusalem artichoke",
                    "jicama",
                    "kale",
                    "kidney bean",
                    "kohlrabi",
                    "lavender",
                    "leek ",
                    "legume",
                    "lemon grass",
                    "lentils",
                    "lettuce",
                    "lima bean",
                    "mamey",
                    "mangetout",
                    "marjoram",
                    "mung bean",
                    "mushroom",
                    "mustard green",
                    "navy bean",
                    "new zealand spinach",
                    "nopale",
                    "okra",
                    "onion",
                    "oregano",
                    "paprika",
                    "parsley",
                    "parsnip",
                    "patty pan",
                    "pea",
                    "pinto bean",
                    "potato",
                    "pumpkin",
                    "radicchio",
                    "radish",
                    "rhubarb",
                    "rosemary",
                    "runner bean",
                    "rutabaga",
                    "sage",
                    "scallion",
                    "shallot",
                    "skirret",
                    "snap pea",
                    "soy bean",
                    "spaghetti squash",
                    "spinach",
                    "squash",
                    "sweet potato",
                    "tabasco pepper",
                    "taro",
                    "tat soi",
                    "thyme",
                    "topinambur",
                    "tubers",
                    "turnip",
                    "wasabi",
                    "water chestnut",
                    "watercress",
                    "white radish",
                    "yam",
                    "zucchini"
                ],
                "herbs": [
                    "Angelica",
                    "Basil",
                    "Holy Basil",
                    "Thai Basil",
                    "Bay leaf",
                    "Indian Bay leaf",
                    "Boldo",
                    "Borage",
                    "Chervil",
                    "Chives",
                    "Garlic Chives",
                    "Cicely",
                    "Coriander leaf",
                    "Cilantro",
                    "Bolivian Coriander",
                    "Vietnamese Coriander",
                    "Culantro",
                    "Cress",
                    "Curry leaf",
                    "Dill",
                    "Epazote",
                    "Hemp",
                    "Hoja santa",
                    "Houttuynia cordata",
                    "Hyssop",
                    "Jimbu",
                    "Kinh gioi",
                    "Lavender",
                    "Lemon balm",
                    "Lemon grass",
                    "Lemon myrtle",
                    "Lemon verbena",
                    "Limnophila aromatica",
                    "Lovage",
                    "Marjoram",
                    "Mint",
                    "Mugwort",
                    "Mitsuba",
                    "Oregano",
                    "Parsley",
                    "Perilla",
                    "Rosemary",
                    "Rue",
                    "Sage",
                    "Savory",
                    "Sansho",
                    "Shiso",
                    "Sorrel",
                    "Tarragon",
                    "Thyme",
                    "Woodruff"
                ],
                "spices": [
                    "Aonori",
                    "Ajwain",
                    "Allspice",
                    "Amchoor",
                    "Anise",
                    "Star Anise",
                    "Asafoetida",
                    "Camphor",
                    "Caraway",
                    "Cardamom",
                    "Black Cardamom",
                    "Cassia",
                    "Celery powder",
                    "Celery seed",
                    "Charoli",
                    "Chenpi",
                    "Cinnamon",
                    "Clove",
                    "Coriander seed",
                    "Cubeb",
                    "Cumin",
                    "Nigella sativa",
                    "Bunium persicum",
                    "Dill",
                    "Dill seed",
                    "Fennel",
                    "Fenugreek",
                    "Fingerroot",
                    "Greater Galangal",
                    "Lesser Galangal",
                    "Garlic",
                    "Ginger",
                    "Aromatic Ginger",
                    "Golpar",
                    "Grains of Paradise",
                    "Grains of Selim",
                    "Horseradish",
                    "Juniper berry",
                    "Kokum",
                    "Korarima",
                    "Dried Lime",
                    "Liquorice",
                    "Litsea cubeba",
                    "Mace",
                    "Mango-ginger",
                    "Mastic",
                    "Mahlab",
                    "Black Mustard",
                    "Brown Mustard",
                    "White Mustard",
                    "Nigella",
                    "Njangsa",
                    "Nutmeg",
                    "Alligator Pepper",
                    "Brazilian Pepper",
                    "Chili Pepper",
                    "Cayenne pepper",
                    "Paprika",
                    "Long Pepper",
                    "Peruvian Pepper",
                    "East Asian Pepper",
                    "Sichuan Pepper",
                    "Sansho",
                    "Tasmanian Pepper",
                    "Black Peppercorn",
                    "Green Peppercorn",
                    "White Peppercorn",
                    "Pomegranate seed",
                    "Poppy seed",
                    "Radhuni",
                    "Rose",
                    "Saffron",
                    "Salt",
                    "Sarsaparilla",
                    "Sassafras",
                    "Sesame",
                    "Shiso",
                    "Sumac",
                    "Tamarind",
                    "Tonka bean",
                    "Turmeric",
                    "Uzazi",
                    "Vanilla",
                    "Voatsiperifery",
                    "Wasabi",
                    "Yuzu",
                    "Zedoary",
                    "Zereshk",
                    "Zest"
                ],
                "mixtures": [
                    "Adjika",
                    "Advieh",
                    "Baharat",
                    "Beau Monde seasoning",
                    "Berbere",
                    "Bouquet garni",
                    "Buknu",
                    "Chaat masala",
                    "Chaunk",
                    "Chili powder",
                    "Crab boil",
                    "Curry powder",
                    "Doubanjiang",
                    "Douchi",
                    "Duqqa",
                    "Fines herbes",
                    "Five-spice powder",
                    "Garam masala",
                    "Garlic powder",
                    "Garlic salt",
                    "Gochujang",
                    "Harissa",
                    "Hawaij",
                    "Herbes de Provence",
                    "Idli podi",
                    "Jamaican jerk spice",
                    "Khmeli suneli",
                    "Lemon pepper",
                    "Mitmita",
                    "Mixed spice",
                    "Montreal steak seasoning",
                    "Mulling spices",
                    "Old Bay Seasoning",
                    "Onion powder",
                    "Panch phoron",
                    "Persillade",
                    "Powder-douce",
                    "Pumpkin pie spice",
                    "Qâlat daqqa",
                    "Quatre épices",
                    "Ras el hanout",
                    "Recado rojo",
                    "Sharena sol",
                    "Shichimi",
                    "Tabil",
                    "Tandoori masala",
                    "Vadouvan",
                    "Yuzukosho",
                    "Za'atar"
                ]
            }
        }
    },
    methods: {
        navigateResults(direction) {
            if (direction === 'down' && this.highlightedIndex < this.searchResults.length - 1) {
                this.highlightedIndex++;
            } else if (direction === 'up' && this.highlightedIndex > 0) {
                this.highlightedIndex--;
            }
        },
        performSearch() {
            const query = this.searchQuery.trim().toLowerCase();
            if (query.length === 0) {
                this.searchResults = [];
                return;
            }
            this.searchResultsFruits = this.listOfAvailableIngredients["fruits"].filter((ingredient) => {
                return ingredient.toLowerCase().includes(query.toLowerCase());
            });
            this.searchResultsVegetables = this.listOfAvailableIngredients["vegetables"].filter((ingredient) => {
                return ingredient.toLowerCase().includes(query.toLowerCase());
            });
            this.searchResultsHerbs = this.listOfAvailableIngredients["herbs"].filter((ingredient) => {
                return ingredient.toLowerCase().includes(query.toLowerCase());
            });
            this.searchResultsSpices = this.listOfAvailableIngredients["spices"].filter((ingredient) => {
                return ingredient.toLowerCase().includes(query.toLowerCase());
            });
            this.searchResultsMixtures = this.listOfAvailableIngredients["mixtures"].filter((ingredient) => {
                return ingredient.toLowerCase().includes(query.toLowerCase());
            });
            this.searchResults = [...this.searchResultsFruits, ...this.searchResultsVegetables, ...this.searchResultsHerbs, ...this.searchResultsSpices, ...this.searchResultsMixtures];
        },
        addIngredient(ingredient) {
            if (ingredient instanceof Event || typeof ingredient === 'undefined') {
                ingredient = this.searchResults[this.highlightedIndex];
            }

            const trimmedIngredient = ingredient.trim();
            // Logic to add ingredient to store
            this.$store.state.ingredients = [...this.$store.state.ingredients, trimmedIngredient];
            this.searchQuery = ''; // Reset the search query
            this.searchResults = []; // Reset the search results
        },
        clearSearchResults() {
            this.searchResults = []; // Clear the search results
        },
    }
}
</script>
<style scoped>
    .recommend-recipe {
        padding: 10%;
    }

    .form-control {
        width: 39%;
        margin: 2% 5% 0.3%;
        padding: 3 5%;
        border-radius: 6px;
        border: 1px solid #ddd;
    }

    .highlighted {
        background-color: #e0e0e0; 
    }

    .search-functionality {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
        position: relative;
    
        transition: 1s;
        animation: reveal 0.7s forwards;
        opacity: 0;
        transform: translateY(100px);
    }

    @keyframes reveal {
        100% {
            opacity: 1;
            transform: translateY(0px);
        }
    }   

    .results-dropdown {
        border: 1px solid #ddd; 
        max-height: 200px; 
        overflow-y: auto; 
        background-color: white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2); 
        position: absolute; 
        width: 39%;
        z-index: 1000; 
        border-radius: 0 0 8px 8px; 

        position: absolute;
        top: 100%; 
    }

    .results-dropdown div {
        padding: 8px 12px; 
        cursor: pointer; 
        border-bottom: 1px solid #eee; 
    }

    .results-dropdown div:hover {
        background-color: #f0f0f0; 
    }

    .highlighted {
        background-color: #bde4ff; 
        color: #333; 
    }
</style>