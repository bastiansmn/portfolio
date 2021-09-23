<template>
   <div class="about">
      <div class="bubble blue-gradient __big" style="
         right: -150px;
         top: 146px;
      "></div>

      <div class="content">
         <div class="text">
            <div class="who_am_i">
               <h1>
                  {{
                     this.getLang
                        ? text.who_am_i.title.en
                        : text.who_am_i.title.fr
                  }}
               </h1>
               <p>
                  {{
                     this.getLang
                        ? text.who_am_i.text.en
                        : text.who_am_i.text.fr
                  }}
               </p>
            </div>
         </div>
         <div class="programming__languages tilting">
            <div :key="lang.classname" v-for="lang of programming_languages"
               class="language"
            >
               <span class="name">{{ lang.name }}</span>
               <!-- <span class="percentage">{{ lang.percentage }}%</span> -->
               <div class="bar">
                  <div
                        :class="'progress ' + lang.classname"
                        :style="`--width: ${lang.percentage}%`"
                  ></div>
               </div>
            </div>

            <div class="resume">
               <a href="">
                  {{
                     this.getLang
                        ? text.resume.en
                        : text.resume.fr
                  }}
               </a>
            </div>
         </div>
      </div>
   </div>
</template>

<script>
import programming_languages from "../../assets/programming_languages";
import text from "../../assets/text";
import { mapGetters } from "vuex";
import vanillaTilt from "https://cdn.skypack.dev/vanilla-tilt@1.7.0";

export default {
   name: "About",
   computed: {
      ...mapGetters(['getLang'])
   },
   mounted() {
      vanillaTilt.init(document.querySelectorAll(".tilting"), {
         max: 2,
         speed: 1000,
         perspective: 700,
         reverse: true,
         reset: false,
         startX: -10,
      });


      let delay = 0;
      for (let language in this.programming_languages) {
         const lang = this.programming_languages[language];
         const div = document.querySelector(`.${lang.classname}`);
         div.style.animationDelay = `${delay}ms`;
         delay += 100;
         setTimeout(_ => {
            div.style.width = `${lang.percentage}%`;
         }, 2000)
      }
   },
   data() {
      return {
         programming_languages,
         text
      }
   }
}
</script>

<style scoped>
.about {
   position: relative;
   height: 80vh;
   width: 100%;

   display: flex;
   align-items: center;
   justify-content: center;
}

.content {
   height: 75%;
   width: 80%;

   display: flex;
   align-items: center;
   justify-content: space-between;
}

.content > div {
   width: calc(48% - 44px);
   height: calc(100% - 44px);
}

.text {
   display: flex;
   flex-direction: column;
   align-items: center;
   justify-content: space-between;
}

.programming__languages {
   height: 78% !important;
   margin-block: 10px;
   background: rgba(255, 255, 255, 0.2);
   box-shadow: 20px 20px 50px rgba(0, 0, 0, .5);
   backdrop-filter: blur(13px);
   border-radius: 21px;

   z-index: 1000;
   display: flex;
   flex-direction: column;
   align-items: center;
   justify-content: space-between;

   padding: 22px;
}

.language {
   display: flex;
   align-items: center;
   justify-content: space-between;

   width: 100%;
   height: 22px;
}

/*
.language > .name {
   display: block;
   opacity: 1;
}

.language > .percentage {
   display: none;
   opacity: 0;
}

.language:hover > .name {
   display: none;
   opacity: 0;
}

.language:hover > .percentage {
   display: block;
   opacity: 1;
   color: var(--primary);
}
 */


.bar {
   width: 72%;
   height: calc(100% - 6px);
   display: flex;
   align-items: center;
   justify-content: flex-start;
   background-color: var(--white);
   border-radius: 8px;
   padding: 3px;
}

.progress {
   height: 100%;
   background-color: var(--primary);
   border-radius: 6px;
   width: 10%;

   animation: width 2s ease-in-out;
}

.resume {
   width: 100%;
   height: 60px;
   display: flex;
   align-items: center;
   justify-content: center;
}

.resume > a {
   height: 30px;
   display: flex;
   align-items: center;
   justify-content: center;
   background-color: var(--primary);
   border-radius: 6px;
   padding-inline: 10px;
   color: var(--white);
   text-decoration: none;
   font-size: 14px;
}

.resume > a:hover {
   transform: scale(1.03);
}

.who_am_i > h1 {
   margin-block: 0;
   color: var(--primary);
   font-size: 40px;
}

.who_am_i > p {
   font-size: 14px;
   margin-block: 20px;

   max-width: 400px;
}

@keyframes width {
   from {
      width: 10%;
   }
   to {
      width: var(--width);
      border-radius: 6px;
   }
}
</style>