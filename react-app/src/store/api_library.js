export async function fetchAllLoans() {
    const options = {};
    options.method = 'GET';
    const url = `/api/loans/`
    const res = await window.fetch(url, options);
    if (res.status >= 400) throw res;
    return res;
}

export async function fetchOneLoan(id) {
    const options = {};
    options.method = 'GET';
    const url = `/api/loans/${id}`
    const res = await window.fetch(url, options);
    if (res.status >= 400) throw res;
    return res;
}

export async function editLoan(payload) {
    const options = {};
    options.method = 'PUT';
    options.headers = {};
    options.body = JSON.stringify(payload);
    options.headers['Content-Type'] = 'application/json';
    const url = `/api/loans/${payload.id}`
    const res = await window.fetch(url, options);
    if (res.status >= 400) throw res;
    return res;
}

export async function postLoan(payload) {
    console.log("in the function)");
    const options = {};
    options.method = 'POST';
    options.headers = {};
    options.body = JSON.stringify(payload);
    options.headers['Content-Type'] = 'application/json';
    const url = `/api/loans/`
    const res = await window.fetch(url, options);
    if (res.status >= 400) {
        console.log(">>>>400")
        const data = res.json();
        console.log("data dot errors", data.errors)
    };
    return res;
}
