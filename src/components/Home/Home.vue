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
               class="avatar card tilt"
               src="src/assets/avatar.jpg"
               alt="Bastian Somon"
         />
         <div class="presentation__text">
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

      <ContinueButton />
   </div>
</template>

<script>
import vanillaTilt from "vanilla-tilt";
import text from "../../assets/text.js";
import {mapGetters} from "vuex";
import ContinueButton from "./ContinueButton.vue";

export default {
   name: "Home",
   components: {ContinueButton},
   mounted() {
      vanillaTilt.init(document.querySelectorAll(".tilt"), {
         max: 7,
         speed: 1000,
         perspective: 700,
         reverse: true,
         reset: false,
         startX: 7,
         startY: -5,
      });
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
.section_active .presentation__text {
	animation-name: rtl;
}

.home[data-color] {
   background: attr(data-color, red);
}

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

.presentation__text > h1 {
   font-size: 40px;
   color: var(--primary);
   margin-block: 12px;
}

.presentation__text > p {
   font-size: 15px;
   margin-block: 0;
}
</style>