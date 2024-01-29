<template>
    <div class="consumption-stats">
        <div class="section-1">
            <ConsumptionTable />
        </div>
    </div>
</template>
<script>
import ConsumptionTable from '@/components/Statistics/ConsumptionTable.vue';

export default {
    name: 'ConsumptionStats',
    components: {
        ConsumptionTable,
    },
}
</script>
<style scoped>
    
</style>