import {createStore} from "vuex";

export default createStore({
    state: {
        eng: true
    },
    mutations: {
        SWITCH_LANG(state) {
            state.eng = !state.eng;
        },
    },
    actions: {
        switchLang(context) {
            context.commit('SWITCH_LANG');
        }
    },
    getters: {
        getLang: state => {
            return state.eng;
        }
    }
})