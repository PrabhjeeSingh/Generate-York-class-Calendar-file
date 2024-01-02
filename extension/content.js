// Function to extract data
function extractTimetableData() {
    const timetableData = [];
    const rows = document.querySelectorAll('table.timetable tbody tr');

    for (let i = 1; i < rows.length; i++) {
        const cells = rows[i].querySelectorAll('td.timetablecell');
        const time = cells[0].innerText.trim();
        const courseData = {
            time,
            Monday: cells[1].innerText.trim(),
            Tuesday: cells[2].innerText.trim(),
            Wednesday: cells[3].innerText.trim(),
            Thursday: cells[4].innerText.trim(),
            Friday: cells[5].innerText.trim()
        };
        timetableData.push(courseData);
    }

    return timetableData;
}

const timetableData = extractTimetableData();
console.log('Extracted Timetable Data:', timetableData);




// Send the extracted data to the background script
chrome.runtime.sendMessage({ action: 'extractData', data: extractTimetableData() });
