<body>

<header>
<h1>Banking Management System with MySQL Database</h1>
</header>

<section>
<h2>Overview</h2>
<p>This Python project is a Banking Management System that is integrated with a MySQL database. The system allows users to perform various banking operations, such as creating accounts, depositing and withdrawing funds, transferring money, and viewing transaction history.</p>
</section>

<section>
<h2>Features</h2>
<ul>
<li><strong>Account Management:</strong> Users can create new accounts, view account details, and update account information.</li>
<li><strong>Transaction Operations:</strong> Perform deposit, withdrawal, and fund transfer operations securely.</li>
<li><strong>Transaction History:</strong> View transaction history to keep track of all account activities.</li>
<li><strong>MySQL Database Integration:</strong> All data is stored and managed using a MySQL database, ensuring data persistence.</li>
</ul>
</section>

<section>
<h2>Requirements</h2>
<ul>
<li>Python 3.7</li>
<li>MySQL Database</li>
<li>MySQL Connector Python library (install using <code>pip install mysql-connector-python</code>)</li>
</ul>
</section>

<section>
<h2>Installation</h2>
<ol>
<li>Clone the repository:</li>
<pre><code>git clone https://github.com/prabhjeetsinghk/Banking-Management-System.git</code></pre>
<li>Set up the MySQL database by executing the SQL script provided in the <code>database_setup.sql</code> file.</li>
<li>Configure the database connection in the <code>config.py</code> file by providing your MySQL database credentials.</li>
<li>Run the application:</li>
<pre><code>python main.py</code></pre>
</ol>
</section>

<section>
<h2>Usage</h2>
<ol>
<li>Run the application and follow the on-screen instructions.</li>
<li>Choose the desired operation from the menu.</li>
<li>Input the required information, such as account details, amount, etc.</li>
<li>View transaction history to check the status of transactions.</li>
</ol>
</section>

<section>
<h2>Project Structure</h2>
<ul>
<li><code>main.py:</code> Main entry point for the application.</li>
<li><code>bank.py:</code> Contains the core banking operations and logic.</li>
<li><code>database.py:</code> Handles database interactions and queries.</li>
<li><code>config.py:</code> Configuration file for database credentials.</li>
<li><code>database_setup.sql:</code> SQL script to set up the required database tables.</li>
</ul>
</section>

<section>
<h2>Contribution</h2>
<p>Contributions are welcome! If you find any issues or want to enhance the project, feel free to open a pull request.</p>
</section>

<footer>
<p>&copy; 2024 Prabhjeet Singh</p>
</footer>

</body>
