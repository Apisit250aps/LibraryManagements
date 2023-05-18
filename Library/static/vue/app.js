// import Vue from 'https://unpkg.com/vue@3/dist/vue.global.js'

const Vue = require('https://unpkg.com/vue@3/dist/vue.global.js')
const testcomponent = require('/test.vue')



const app = Vue.createApp({})

app.component('test', testcomponent)


app.mount('#index')
