export default function handleResponseFromAPI(promise) {
  const myPromise = promise
    .then(() => ({ status: 200, body: 'success' }))
    .catch(() => Error())
    .finally(() => console.log('Got a response from the API'));
  return myPromise;
}
