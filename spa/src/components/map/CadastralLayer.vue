<template>
  <GeoportalLayer
    layer="CADASTRALPARCELS.PARCELS"
    style_="bdparcellaire"
    format="image/png"
    layer-type="overlay"
    name="Cadastre"
  />
</template>

<script>
import GeoportalLayer from "./GeoportalLayer";

export default {
  components: { GeoportalLayer },
};
</script>
