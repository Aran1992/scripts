const fs = require('fs');
const path = require('path');
const root = 'C:\\Users\\25722\\Downloads\\ver_1';
fs.readdirSync(root).forEach((file, i) => {
    const filepath = path.join(root, file);
    fs.renameSync(filepath, path.join(root, `${10086 + i}${path.extname(filepath)}`));
});
fs.readdirSync(root).forEach((file, i) => {
    const filepath = path.join(root, file);
    fs.renameSync(filepath, path.join(root, `${i}${path.extname(filepath)}`));
});