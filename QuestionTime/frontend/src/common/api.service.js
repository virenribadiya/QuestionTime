const axios = require("axios");

axios.defaults.xsrfCookieName = "csrftoken"; // generating token value
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"; // adding it as a header for each request

export {axios};