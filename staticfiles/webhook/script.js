        // Wait for the DOM to load
        document.addEventListener('DOMContentLoaded', (event) => {
            let successMessage = document.getElementById('success-message');
            // Check if there is a message to display
            if (successMessage && successMessage.innerText.trim() !== '') {
            successMessage.style.display = 'block';
            successMessage.style.opacity = 1;
            // Set a timeout to hide the message after 10 seconds
            let timeout = setTimeout(() => {
                successMessage.style.opacity = 0;
            }, 10000);
            // If the user hovers over the message, clear the timeout and hide the message immediately
            successMessage.addEventListener('mouseover', () => {
                clearTimeout(timeout);
                successMessage.style.opacity = 0;
            });
            // After the transition ends, set display to 'none'
            successMessage.addEventListener('transitionend', () => {
                successMessage.style.display = 'none';
            });
            }
        });
        // JavaScript code
        document.addEventListener('DOMContentLoaded', function() {
            // Fetch alert data from backend
            var xhr = new XMLHttpRequest();
            xhr.open('GET', '/api/alerts/', true);
            xhr.onload = function() {
                if (xhr.status == 200) {
                    var alerts = JSON.parse(xhr.responseText);
                    // Populate table with alert data
                    populateTable(alerts);
                    localStorage.setItem('alerts', JSON.stringify(alerts))
                }
            };
            xhr.send();
        });
    
        function formatDateStringSimple(dateString) {
            const d = new Date(dateString);
            return `${d.getFullYear()}년 ${(d.getMonth()+1).toString().padStart(2, '0')}월 ${d.getDate().toString().padStart(2, '0')}일 ${d.getHours().toString().padStart(2, '0')}:${d.getMinutes().toString().padStart(2, '0')}`;
        }
        function populateTable(alerts) {
            var tableBody = document.getElementById('alert-table-body');
            alerts.forEach(function(alert) {
                var row = tableBody.insertRow();
                row.insertCell(0).textContent = alert.name;
                row.insertCell(1).textContent = alert.severity;
                row.insertCell(2).textContent = alert.summary;
                row.insertCell(3).textContent = alert.description;
                row.insertCell(4).textContent = formatDateStringSimple(alert.created_at);
            });
        }
    
        // Function to generate and download Excel file
        document.getElementById('download-btn').addEventListener('click', function() {
            generateAndDownloadExcel();
        });
    
        function generateAndDownloadExcel() {
            // Retrieve data from the table
            var alerts = JSON.parse(localStorage.getItem('alerts') || '[]')
            var csvContent = 'data:text/csv;charset=utf-8,\uFEFF';
    
            csvContent += "Name,Severity,Summary,Description,Created At" + "\n";
    
            alerts.forEach(function(alert) {
                let row = `"${alert.name}","${alert.severity}","${alert.summary}","${alert.description}","${formatDateStringSimple(alert.created_at)}"`;
                csvContent += row + "\n";
            });
    
            // Trigger download
            var encodedUri = encodeURI(csvContent);
            var link = document.createElement('a');
            link.setAttribute('href', encodedUri);
            link.setAttribute('download', 'alerts.csv');
            document.body.appendChild(link);
            link.click();
        }
    
        // Show confirmation popup when delete button is clicked
        document.getElementById('delete-entries-btn').addEventListener('click', function() {
            var modal = document.getElementById('confirmationModal');
            modal.style.display = 'block';
        });
    
        // Hide confirmation popup if cancel button is clicked
        document.getElementById('cancelDeleteBtn').addEventListener('click', function() {
            var modal = document.getElementById('confirmationModal');
            modal.style.display = 'none';
        });
    
        // Handle delete confirmation
        document.getElementById('confirmDeleteBtn').addEventListener('click', function() {
            // Make AJAX request to delete entries
            fetch('/delete_entries/', {
                method: 'POST',
            })
            .then(response => {
                // Reload the page after deletion
                location.reload();
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });