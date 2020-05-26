const mysql = require("mysql");

const connection = mysql.createConnection({
    host:"94.130.57.82",
    user:"appsplat_semih",
    password:"semihsemih123",
    database:"appsplat_semih"
});

connection.connect();

module.exports = {
    db : connection
};
