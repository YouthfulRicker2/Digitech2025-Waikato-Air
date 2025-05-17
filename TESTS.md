# Tests

- Age Boundary Test
- Destination Input Error Test
- Name Input Correction Test
- Remaining Seat Input Test
- Discount Test
    - Child
    - Senior
    - Urgency/Seat Scarcity
    - Urgency
- Data Save Test
- Data Retrieval Test
- Algebra Test
- Replay Test

## Test Descriptions

When running these tests, unless stated otherwise, enter the [control variables below](## Control Testing Values).

### Age Boundary Test
- When asked for age, enter values `0`, `161`, and `273` in succession. This should be simple as they should all fail and ask for a re-entry. 
- After you've entered the incorrect values, enter `159`, and `1` in separate runs of the program, these should go through, and also trigger their respective discounts.
### Destination Input Error Test
- Enter gibberish such as: `4mula1`, `#WaWzA453`, and random cities such as: `Tokyo`, `Adelaide`.
- These should all fail and trigger a re-entry, use the control variables to confirm the route calculation is correct; *(Rotorua -> Hamilton == $100)*
### Name Input Correction Test
- Try inputting the following 'names': `Princ3 J0n3$`, `Kr0nk 3Lph465`. These should trigger a re-entry for containing numerical values.
- Enter the control variable name *(Klanken Mcklanketh)* in entirely lowercase, and entirely uppercase. Both times it should show up capitalised properly in the email.
### Remaining Seat Input Test
- Input `0` and `201` when asked how many seats are remaining. They should both fail and trigger a re-entry.
- In two further booking attempts, enter `1` and `199` for seats remaining. These should both work, and '1' should trigger the Seat Scarcity discount.
### Time Entry Test
- Follow the control variables, but for the month, first enter `13`, and then `0`. These should trigger a re-entry.
- Now for the date, enter `32` and `0`, these should also trigger a re-entry.
- Now simply follow the control variables through. That should work perfectly.
### Discount Test
- As the age discounts would've been confirmed while doing the age entry test, and the seat scarcity discount would've been confirmed during the remaining seats input test, the singular discount that hasn't been tested yet is the lower urgency discount, which is activated when there's less than 50, and more than 20 days until the flight. To test this, enter your current date, but increase the month by one. 
- You should end up with $90 due to the 10% discount.
### Data Save Test
- Delete the `waikato_air_bookings.csv` file before testing.
- Go through the book process, and you should see this at the end: `Booking appended to waikato_air_bookings.csv.`
### Data Retrieval Test
- Type 'view' when running the program, and enter the name of the control testing value fellow, and the data should all match the values below.
### Mailto Test
- When asked if to mail the email now when booking, answer `yes` and if it's working, your email client will automatically open with the subject and contents already within the email.
- When you say `no` it should just leave you alone, like a nice calm gorilla.

## Control Testing Values
Name: `Klanken Mcklanketh`
Age: `43`
Flight Date: Precisely 1 Year from Test Date
Departure: `Rotorua`
Destination: `Hamilton`
Remaining Seats: `143`
Expected Cost Output: $100 (Base Rotorua-Hamilton Cost)

## Testing

iteration1 = Commit ID: d12d69a658eca7a1fd86701c82d5b5180d8b2085
iteration2 = Commit ID: e1cd4976e33542850a747a3c35224ac6446e0102
iteration3 = Commit ID: 15d0dcaf02b738591ca4814b99d8b4e6ca036a57

Success indicates that the iteration passed the test,
N/A indicates that the feature wasn't implemented in that iteration.

|                            Test Table                           | iteration1  | iteration2  | iteration3  |
|-----------------------------------------------------------------|-------------|-------------|-------------|
| [Age Boundary Test](###Age Boundary Test)                       |   Success   |   Success   |   Success   |
| [Destination Input Error Test](###Destination Input Error Test) |   Success   |   Success   |   Success   |
| [Name Input Correction Test](###Name Input Correction Test)     |   Success   |   Success   |   Success   |
| [Remaining Seat Input Test](###Remaining Seat Input Test)       |   Success   |   Success   |   Success   |
| [Time Entry Test](###Time Entry Test)                           |   Success   |   Success   |   Success   |
| [Discount Test](###Discount Test)                               |   Success   |   Success   |   Success   |
| [Data Save Test](###Data Save Test)                             |     N/A     |   Success   |   Success   |
| [Data Retrieval Test](###Data Retrieval Test)                   |     N/A     |   Success   |   Success   |
| [Mailto Test](###Mailto Test)                                   |     N/A     |     N/A     |   Success   |
