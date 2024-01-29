<template>
    <div class="predict-image">
        <form @submit.prevent="predictImage">
            <div class="form-group">
                <input type="file" class="image-uplaod form-control" ref="fileInput" id="image" @change="handleFileUpload">
            </div>
        </form>
    </div>
</template>

<script>
    export default {
        name: 'PredictImage',
        data() {
            return {
                file: null,
            }
        },
        methods: {
            handleFileUpload() {
                this.file = this.$refs.fileInput.files[0];
                console.log(this.file);
                this.predictImage(); // Call signup method to submit the form
            },
            predictImage() {
                if (!this.file) {
                    alert("Please select a file first.");
                    return;
                }
                const formData = new FormData();
                formData.append('file', this.file);
                console.log(formData);
                const requestOptions = {
                    method: 'POST',
                    body: formData,
                    redirect: 'follow'
                    };
                fetch(this.$store.state.url + 'predict', requestOptions)
                .then(response => response.json())
                .then(data => {
                    console.log(data["result"]);
                    this.$store.state.ingredients = [...this.$store.state.ingredients, data["result"]];
                    this.$refs.fileInput.value = '';
                })
                .catch(error => {
                    console.error(error);
                });
            }
        },
    }
</script>

<style scoped>
    .form-group {
        margin: 0 5%;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .image-uplaod {
        width: 43.5%;
        margin-top: 0;
        margin-bottom: 0;
        text-decoration: none;
        border-radius: 6px;
    }

    .predict-image {
        transition: 1s;
        animation: reveal 0.7s forwards;
        opacity: 0;
        transform: translateY(-100px);
    }

    @keyframes reveal {
        100% {
            opacity: 1;
            transform: translateY(0px);
        }
    }

    .form-control {
        color: #FF7F50;
    }
</style>
