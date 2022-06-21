<template>
  <div class="account-error-list">
    <!-- field를 키로 errors 순환-->
    <p v-for="(errors, field) in authError" :key="field">
      <!-- 해당하는 field 보여주고 -->
      {{ field }}
      <ul>
        <!-- idx를 키로 error 순환 -->
        <li v-for="(error, idx) in errors" :key="idx">
          <!-- error 보여주고 -->
          {{ error }}
        </li>
      </ul>
    </p>
  </div>
</template>

<script>
  import { mapGetters } from 'vuex'

  export default {
    name: 'AccountErrorList',
    computed: {
      ...mapGetters(['authError'])
    },
  }
</script>

<style>

</style>