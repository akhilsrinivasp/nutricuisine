<template> 
    <div class="auth" align = center>
        <LoginComp />
    </div>
</template>

<script>
    import LoginComp from '@/components/LoginComp.vue'
    export default {
        name: 'LoginView', 
        components: {
            LoginComp
        }
    }
</script>

<style scoped>
    .auth {
        animation: reveal 0.5s forwards;
        opacity: 0;
        transform: translateY(-50px);
    }
    @keyframes reveal {
        100% {
            opacity: 1;
            transform: translateX(0px);
        }
    }
</style>