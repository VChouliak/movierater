import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http'

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  baseUrl = 'http://127.0.0.1:8000/api/movies/';
  headers = new HttpHeaders({
    'Content-Type': 'application/json',
    Authorization : 'Token 03cabca16a1f32a065def5ae5cd75a51eb9cab19'
    
  });

  private movies = ['Terminator', 'Predator'];

  constructor(private httpClient: HttpClient) { }

  getMovies() {
    return this.httpClient.get(this.baseUrl, { headers: this.headers });
  }
}
