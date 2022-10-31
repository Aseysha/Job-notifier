from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

jobs_data = [{
        "id": "css_123",
        "title": "Web Developer",
        "description": "A web developer make and maintain websites." +
        "They are in charge of a site's overall look and feel. Web develoWeb developers also handle the technical aspects of a website. ",
    },
    {
        "id": "css_456",
        "title": "Cloud Engineer",
        "description": "description" " Primary responsibilities include developing and implementing policies for the use of cloud services," + 
        " managing requests for new technology, establishing a secure cloud environment, and ensuring appropriate availability of services," + 
        " also known as uptime."
    }]

@app.get("/")
def health():
    return {"health": "OK"}

@app.get("/job")
def getJobs():
    return jobs_data

@app.get("/job/{id}")
def getJob(id):
    for job in jobs_data:
        if (job["id"] == id): 
            return job
    raise HTTPException (status_code=404, detail="Job with id" + id + "not found")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)