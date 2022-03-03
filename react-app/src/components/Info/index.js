function Info() {
    return (
        <div className="content-container">
            <div>
                <h1>API Library</h1>
                <p>For this code challenge, all functions work in the console of the browser.</p>

                <p><code>fetchAllLoans()</code> - <code>GET</code> request for all loans</p>
                <p><code>fetchOneLoan(id)</code> - <code>GET</code> request for one specific loan</p>
                <p><code>postLoan(payload)</code> - <code>POST</code> request for a new loan</p>
                <p><code>editLoan(payload)</code> - <code>PUT</code> request one specific loan</p>
                <h2>Syntax:</h2>
                <p>The backend route for <code>postLoan</code> expects a payload structured as follows:</p>
                <p><code>
                    const payload = &#123;<br />
                    &emsp;amount,<br />
                    &emsp;interest_rate,<br />
                    &emsp;length_months,<br />
                    &emsp;monthly_payment<br />
                    &#125;
                </code></p>
                <br />
                <br />
                <p>The backend route for <code>editLoan</code> expects a payload structured as follows:</p>
                <p>
                    <code>
                        const payload = &#123;<br />
                        &emsp;id,<br />
                        &emsp;amount,<br />
                        &emsp;interest_rate,<br />
                        &emsp;length_months,<br />
                        &emsp;monthly_payment<br />
                        &#125;
                    </code>
                </p>
                <br />
                <br />
                <h2>Example console command:</h2>
                <p>
                    <code>
                        const payload = &#123;<br />
                        &emsp;id: 1,<br />
                        &emsp;amount: 100000,<br />
                        &emsp;interest_rate: 20.4,<br />
                        &emsp;length_months: 10,<br />
                        &emsp;monthly_payment: 11000<br />
                        &#125;
                        const response = await editLoan(payload);<br />
                        const data = await response.json();<br />
                        console.log(data)<br />
                    </code>
                </p>

            </div>
        </div>
    )
}
export default Info;
