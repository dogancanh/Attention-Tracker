const {app, BrowserWindow, ipcMain, ipcRenderer} = require('electron');
const db = require("./connection").db;

function createWindow() {
    // Create the browser window.
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true
        }
    })

    // and load the index.html of the app.
    win.loadFile('index.html')

    // Open the DevTools.
    win.webContents.openDevTools()

    //user-password
    ipcMain.on("key", function (e, data) {
        db.query("SELECT id,password,role from user where id=? and password=?", [data[0], data[1]], (error, results, fields) => {

            if (results == 0) {
                //console.log('Bu neee')
                let message = 'Wrong id-password combination'
                win.webContents.send("sbs", message)

            } else {
                console.log(results[0]["id"]);
                console.log('***********');
                console.log(results[0]["password"]);
                if (results[0]["role"] == 'lecturer') {
                    win.loadFile("userpage_t.html")
                    win.webContents.once('dom-ready', () => {
                        console.log('hocasın seen')
                        db.query("SELECT min,attentionP from attentionstudent ",null,(error,rslt,fields)=>{
                            win.webContents.send("datas",rslt)
                        })
                    })
                } else {
                    win.loadFile('userpage.html')
                    win.webContents.openDevTools()
                    win.webContents.once('dom-ready', () => {
                        win.webContents.send("userinf", results[0]["id"])
                        win.webContents.send("usrid", results[0]["id"])
                        ipcMain.on("usercourse", function (event, args) {
                            win.webContents.send("usrcrs", args)
                        })
                    })
                }
            }
        })
    })
}


// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.whenReady().then(createWindow)

// Quit when all windows are closed.
app.on('window-all-closed', () => {
    // On macOS it is common for applications and their menu bar
    // to stay active until the user quits explicitly with Cmd + Q
    if (process.platform !== 'darwin') {
        app.quit()
    }
})

app.on('activate', () => {
    // On macOS it's common to re-create a window in the app when the
    // dock icon is clicked and there are no other windows open.
    if (BrowserWindow.getAllWindows().length === 0) {
        createWindow()
    }
})
