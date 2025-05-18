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

### Name Input Boundary Test
- iteration1-3
    - When asked for a name, enter the name `Seraphina Nyx Thornevale of House Aerendell Virelith`, as this is over 50 characters *(52)*, it should immediately reject it and ask again.
    - Next enter `Seraphinyx Thornevale of House Aerendell Virelith` and it should go through, being precisely 49 characters.
- iteration4
    - Try entering `Serephiel Drax Nyvenn Jyrethel` of as the first name and `House Virellanthas Stormrend` as the last name — both are over 25 characters and should be rejected.
    - Then enter `Serephielyvenn` as the first name and `Stormrendirelith` as the last name — both are within the limit and should be accepted.
### Age Boundary Test
- When asked for age, enter values `0`, `161`, and `273` in succession. This should be simple as they should all fail and ask for a re-entry. 
- After you've entered the incorrect values, enter `159`, and `1` in separate runs of the program, these should go through, and also trigger their respective discounts.
### Destination Input Error Test
- Enter gibberish such as: `4mula1`, `#WaWzA453`, and random cities such as: `Tokyo`, `Adelaide`.
- These should all fail and trigger a re-entry, use the control variables to confirm the route calculation is correct; *(Rotorua -> Hamilton == $100)*
### Name Input Correction Test
- iteration1-3
    - Try inputting the following 'names': `Princ3 J0n3$`, `Kr0nk 3Lph465`. These should trigger a re-entry for containing numerical values.
    - Enter the control variable name *(Klanken Mcklanketh)* in entirely lowercase, and entirely uppercase. Both times it should show up capitalised properly in the email.+
- iteration4
    - Try entering the following when prompted for the first or last name: `Princ3`, `J0n3$`, or `3Lph465`. These should all trigger a re-entry message because they contain numbers or symbols.
    - When asked for a valid name, enter `klanken` for the first name and `mcklanketh` for the last name — then repeat using `KLANKEN` and `MCKLANKETH`. Each time, the output should return `Klanken Mcklanketh`, correctly capitalised regardless of how it was typed.
### Remaining Seat Input Test
- iteration1-3
    - Input `0` and `201` when asked how many seats are remaining. They should both fail and trigger a re-entry.
    - In two further booking attempts, enter `1` and `199` for seats remaining. These should both work, and '1' should trigger the Seat Scarcity discount.
- iteration4
    - I have changed the program's max seats to 171, because that's how many seats [Air New Zealand have on their Airbus A320 domestic flights](https://www.airnewzealand.co.nz/seat-map-airbus-a320-171d).
    - Input `0` and `172` when asked how many seats are remaining. They should both fail and trigger a re-entry.
    - In two further booking attempts, enter `1` and `170` for seats remaining. These should both work, and '1' should trigger the Seat Scarcity discount.
### Time Entry Test
- Follow the control variables, but for the month, first enter `13`, and then `0`. These should trigger a re-entry.
- Now for the date, enter `32` and `0`, these should also trigger a re-entry.
- Now simply follow the control variables through. That should work perfectly.
### Date Boundary Test
- When asked to enter the date
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

iteration1 = Commit ID: [c55bafeb8708a22e7767cdc4f5a81295a45ecf8e](https://github.com/YouthfulRicker2/Digitech2025-Waikato-Air/commit/c55bafeb8708a22e7767cdc4f5a81295a45ecf8e)
iteration2 = Commit ID: [a8f1d94b3444efba5e8c4bb9dfedb3f2d96d4d4d](https://github.com/YouthfulRicker2/Digitech2025-Waikato-Air/commit/a8f1d94b3444efba5e8c4bb9dfedb3f2d96d4d4d)
iteration3 = Commit ID: [7fb59f774cb57bfe66500f9f9b40039e68a1fc4e](https://github.com/YouthfulRicker2/Digitech2025-Waikato-Air/commit/7fb59f774cb57bfe66500f9f9b40039e68a1fc4e)
iteration4 = Commit ID: [9dd4af9edb87bad7d56261512fe343c5e3adee7f](https://github.com/YouthfulRicker2/Digitech2025-Waikato-Air/commit/9dd4af9edb87bad7d56261512fe343c5e3adee7f)

Success indicates that the iteration passed the test,
N/A indicates that the feature wasn't implemented in that iteration.

|          Test Table           | iteration1  | iteration2  | iteration3  | iteration4  |
|-------------------------------|-------------|-------------|-------------|-------------|
| Name Entry Boundary Test      |     N/A     |     N/A     |     N/A     |   Success   |
| Age Boundary Test             |   Success   |   Success   |   Success   |   Success   |
| Destination Input Error Test  |   Success   |   Success   |   Success   |   Success   |
| Name Input Correction Test    |   Success   |   Success   |   Success   |   Success   |
| Remaining Seat Input Test     |   Success   |   Success   |   Success   |   Success   |
| Time Entry Test               |   Success   |   Success   |   Success   |   Success   |
| Date Boundary Test            |     N/A     |     N/A     |     N/A     |   Success   |
| Discount Test                 |   Success   |   Success   |   Success   |   Success   |
| Data Save Test                |     N/A     |   Success   |   Success   |   Success   |
| Data Retrieval Test           |     N/A     |   Success   |   Success   |   Success   |
| Mailto Test                   |     N/A     |     N/A     |   Success   |   Success   |
