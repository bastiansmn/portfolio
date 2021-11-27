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
      <div class="anchor">
         <a href="#home"
            @click="setActive('home'); setObserver(false);"
         >{{
               this.getLang
                  ? text.home.en
                  : text.home.fr
            }}
         </a>
         <a href="#about"
            @click="setActive('about'); setObserver(false);"
         >{{
               this.getLang
                     ? text.about.en
                     : text.about.fr
            }}
         </a>
         <a href="#work"
            @click="setActive('work'); setObserver(false);"
         >{{
               this.getLang
                     ? text.work.en
                     : text.work.fr
            }}
         </a>
         <a href="#contact"
            @click="setActive('contact'); setObserver(false);"
         >{{
               this.getLang
                     ? text.contact.en
                     : text.contact.fr
            }}
         </a>
      </div>
   </nav>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import text from "../assets/text.js";
import setActive from "../utils/function";

export default {
   name: "navbar",
   methods: {
      switchLang() {
         this.switchLang();
      },

      setActive,

      ...mapActions(['switchLang', 'setObserver']),
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

.anchor {
   width: 440px;
   display: flex;
   align-items: center;
   justify-content: space-between;
   padding-inline: 5px;
   margin-right: 75px;
   position: relative;
}

.anchor > a {
   text-decoration: none;
   width: 66px;
   color: var(--dark-grey);
   font-size: 15px;
   font-weight: bolder;
   display: flex;
   align-self: center;
   justify-content: center;
}

.anchor > a:hover {
   color: var(--white);
}

.anchor > a.anchor_active {
   color: var(--white);
   transform: scale(1.07);
}

a.anchor_active:before {
   width: 110px;
   height: 110px;
   background-color: var(--white);
   border-radius: 50%;
   animation: anchor-shadow 0.6s ease-in-out;
   --topix: -10px;
   box-shadow: 0 24px 65px var(--topix) rgba(255, 255, 255, 0.3);
   transform: translateY(-111px);
   content: "";
   position: absolute;
   align-self: center;
}

/*
Allows you to add a small light above the anchor you're hovering
It's not the best choice, since it conflicts with the animation,
and moreover, when you finished hovering, it basically remove
the hover, which isn't really nice.


.anchor a:not(.anchor_active):hover:before {
   width: 110px;
   height: 110px;
   background-color: var(--white);
   border-radius: 50%;
   animation: anchor-shadow 0.3s ease-in;
   --topix: -38px;
   box-shadow: 0 24px 65px var(--topix) rgba(255, 255, 255, 0.3);
   transform: translateY(-100%);
   content: "";
   position: absolute;
   align-self: center;
}
 */


.navbar__background {
   background: rgba(25, 27, 41, 0.7);
   box-shadow: 0 3px 7px rgba(0, 0, 0, 0.25);
   backdrop-filter: blur(4px);
}


@keyframes anchor-shadow {
   from {
      box-shadow: 0 24px 65px -50px rgba(255, 255, 255, 0.3);
   }
   to {
      box-shadow: 0 24px 65px var(--topix) rgba(255, 255, 255, 0.3);
   }
}

</style>