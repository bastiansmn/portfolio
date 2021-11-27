<template>
   <div class="home">
      <div class="bubble blue-gradient __big" style="
         left: -150px;
         top: 146px;
      "></div>
      <div class="bubble white-gradient __medium" style="
         right: -43px;
         top: 376px;
      "></div>
      <div class="bubble white-gradient __small" style="
         right: 131px;
         top: 77px;
      "></div>
      <div class="bubble blue-gradient __small" style="
         right: 100px;
         top: 376px;
         --xmove: -10px !important;
         --ymove: -5px !important;
      "></div>

      <div class="introducing">
         <img
               class="avatar card tilting"
               src="src/assets/avatar.jpg"
               alt="Bastian Somon"
         />
         <div class="presentation__text reveal-rtl">
            <p>
               {{
                  this.getLang
                        ? text.introducing.header.en
                        : text.introducing.header.fr
               }}
            </p>
            <h1>
               {{
                  this.getLang
                        ? text.introducing.name.en
                        : text.introducing.name.fr
               }}
            </h1>
            <p>
               {{
                  this.getLang
                        ? text.introducing.p.en
                        : text.introducing.p.fr
               }}
            </p>
         </div>
      </div>

      <ContinueButton class="continue" :link="'#about'">
			<div>
            {{
               this.getLang
                  ? text.continue_button.first.en
                  : text.continue_button.first.fr
            }}
         </div>
         <div>
            {{
               this.getLang
                     ? text.continue_button.second.en
                     : text.continue_button.second.fr
            }}
         </div>
		</ContinueButton>
   </div>
</template>

<script>
import text from "../../assets/text.js";
import {mapGetters} from "vuex";
import ContinueButton from "../utils/ContinueButton.vue";

export default {
   name: "Home",
   components: {ContinueButton},
   mounted() {
		
   },
   computed: {
      ...mapGetters(['getLang'])
   },
   data() {
      return {
         text,
      }
   },
}
</script>

<style scoped>
.home {
   position: relative;
   display: flex;
   justify-content: center;

   height: 80vh;

   width: 100%;
}

.card {
   position: relative;
   margin: 10px;
   overflow: hidden;
   border-radius: 15px;
   box-shadow: 20px 20px 50px rgba(0, 0, 0, .5);
   display: flex;
   align-items: center;
   justify-content: center;
   z-index: 100;
}



.introducing {
   display: flex;
   align-items: center;
   justify-content: space-between;

   width: 65%;
   max-width: 850px;
   min-width: 600px;
   height: 220px;
   margin-top: min(15vh, 150px);
   padding: 10px;

   z-index: 10;
}

.avatar {
   height: 240px;
   width: 240px;
   border-radius: 30px;
}

.presentation__text {
   width: calc(100% - 330px);
   max-width: 450px;
   height: 90%;

   display: flex;
   flex-direction: column;
   align-items: flex-start;
   justify-content: center;
}

.presentation__text:first-child {
   font-size: 16px;
}

.continue {
   position: absolute;
   bottom: 7%;
}
</style>