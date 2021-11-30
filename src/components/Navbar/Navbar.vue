<template>
   <nav class="navbar">
      <div class="toggle-lang">
         <span
            :style="
               this.getLang
                  ? { color: 'var(--white)' }
                  : {  }
            "
         >EN</span>
         <input type="checkbox" :checked="!this.getLang" id="switch" />
         <label for="switch" @click.prevent="switchLang"></label>
         <span
            :style="
               !this.getLang
                  ? { color: 'var(--white)' }
                  : {  }
            "
         >FR</span>
      </div>

		<Links />
   </nav>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import text from "../../assets/text.js";
import Links from "./Links.vue";

export default {
   name: "navbar",
	components: {
		Links,
	},
   methods: {
      switchLang() {
         this.switchLang();
      },

      ...mapActions(['switchLang']),
   },
   computed: {
      ...mapGetters(['getLang']),
   },
   data() {
      return {
         text,
      }
   }
}
</script>

<style scoped>
.navbar {
   width: 100%;
   height: 110px;

   position: fixed;
   top: 0;
   z-index: 9999;

   display: flex;
	flex-direction: row;
   align-self: center;
   justify-content: space-between;
}

.toggle-lang {
   width: 200px;
   height: 100%;

   display: flex;
   align-items: center;
   justify-content: center;
}

input[type=checkbox]{
   height: 0;
   width: 0;
   display: none;
}

label {
   cursor: pointer;
   text-indent: -9999px;
   width: 32px;
   height: 18px;
   background-color: var(--primary);
   display: block;
   border-radius: 9px;
   position: relative;

   margin-inline: 15px;
   transition: none;
}

label:after {
   content: '';
   position: absolute;
   top: 2px;
   left: 2px;
   width: 14px;
   height: 14px;
   background: var(--white);
   border-radius: 90px;
   transition: 0.3s;
}

input:checked + label {
   background: var(--white);
}

input:checked + label:after {
   left: calc(100% - 2px);
   transform: translateX(-100%);
   background-color: var(--primary);
}

label:active:after {
   width: 16px;
}

span {
   color: var(--dark-grey);
}

.navbar__background {
   background: rgba(25, 27, 41, 0.7);
   box-shadow: 0 3px 7px rgba(0, 0, 0, 0.25);
   backdrop-filter: blur(4px);
}
</style>